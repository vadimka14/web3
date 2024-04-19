from typing import Optional, Union
from loguru import logger

from py_okx_async.OKXClient import OKXClient
from py_okx_async.asset.models import TransferTypes, Currency
from py_okx_async.models import OKXCredentials, AccountTypes


class OKXActions:
    def __init__(self, credentials: OKXCredentials):
        self.entrypoint_url = 'https://www.okx.com'
        self.credentials = credentials
        self.okx_client = None
        if self.credentials.completely_filled():
            self.okx_client = OKXClient(credentials=credentials, entrypoint_url=self.entrypoint_url)

    async def all_balances_are_zero(self, amount: float = 0.0) -> bool:
        for subaccount_name in await self.okx_client.subaccount.list():
            balances = await self.okx_client.subaccount.asset_balances(subAcct=subaccount_name, token_symbol='ETH')
            for balance in balances.values():
                if balance.availBal > amount:
                    return False
        return True

    async def collect_funds_from_subaccounts(self):
        for subaccount_name in await self.okx_client.subaccount.list():
            balances = await self.okx_client.subaccount.asset_balances(subAcct=subaccount_name, token_symbol='ETH')
            for balance in balances.values():
                avail_bal = balance.availBal
                if avail_bal > 0:
                    await self.okx_client.asset.transfer(
                        token_symbol='ETH', amount=avail_bal, to_=AccountTypes.Funding, subAcct=subaccount_name,
                        type=TransferTypes.SubToMasterMasterKey
                    )

    async def get_withdrawal_fee(self, token_symbol: str, chain: str) -> Optional[float]:
        token_symbol = token_symbol.upper()
        currencies = await self.okx_client.asset.currencies(token_symbol=token_symbol)
        if token_symbol not in currencies:
            return None

        currency = currencies[token_symbol]
        if chain not in currency:
            return None

        currency_info: Currency = currency[chain]
        if not currency_info.canWd:
            return None

        if currency_info.minFee:
            return currency_info.minFee
        return None

    async def try_to_get_tx_hash(self, wd_id: Union[str, int]) -> Optional[str]:
        wd_id = int(wd_id)
        withdrawal_history = await self.okx_client.asset.withdrawal_history(wdId=wd_id)
        if withdrawal_history and withdrawal_history.get(wd_id) and withdrawal_history.get(wd_id).txId:
            return withdrawal_history.get(wd_id).txId

    async def withdraw(
            self,
            to_address: str,
            amount: Union[float, int, str],
            token_symbol: str,
            chain: str,
    ) -> str:
        failed_text = 'Failed to withdraw from OKX'
        try:
            if not self.okx_client:
                return f'{failed_text}: there is no okx_client'

            fee = await self.get_withdrawal_fee(token_symbol=token_symbol,chain=chain)
            if not fee:
                return f'{failed_text} | can not get fee for withdraw'

            withdrawal_token = await self.okx_client.asset.withdrawal(
                token_symbol=token_symbol, amount=amount, toAddr=to_address, fee=fee, chain=chain
            )
            withdrawal_id = withdrawal_token.wdId
            if withdrawal_id:
                return f'A withdrawal request of {amount} {token_symbol} was sent: ({withdrawal_id}) to {to_address}'

            return f'{failed_text}! withdrawal_id: {withdrawal_id}'

        except BaseException as e:
            logger.exception(f'withdraw: {e}')
            return f'{failed_text}: {e}'