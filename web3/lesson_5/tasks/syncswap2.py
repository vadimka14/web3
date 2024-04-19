import time
import asyncio
import random

from web3.types import TxParams

from eth_async.models import RawContract, TxArgs, TokenAmount
from tasks.base import Base
from data.models import Contracts


class SyncSwap2(Base):
    async def _swap(
            self,
            from_token: RawContract,
            to_token: RawContract,
            pool: RawContract,
            amount: TokenAmount,
            slippage: float = 1.0,
    ):
        from_token_is_eth = from_token.address.upper() == Contracts.WETH.address.upper()

        from_token = await self.client.contracts.default_token(contract_address=from_token.address)
        from_token_name = await from_token.functions.symbol().call()

        to_token = await self.client.contracts.default_token(contract_address=to_token.address)
        to_token_name = await to_token.functions.symbol().call()

        if from_token_name == 'WETH':
            from_token_name = 'ETH'
        if from_token_name == 'WBTC':
            from_token_name = 'BTC'
        if from_token_name == 'ceBUSD':
            from_token_name = 'BUSD'
        if from_token_name == 'USDC.e':
            from_token_name = 'USDC'

        if to_token_name == 'WETH':
            to_token_name = 'ETH'
        if to_token_name == 'WBTC':
            to_token_name = 'BTC'
        if to_token_name == 'ceBUSD':
            to_token_name = 'BUSD'
        if to_token_name == 'USDC.e':
            to_token_name = 'USDC'

        failed_text = f'Failed swap {from_token_name} to {to_token_name} via SyncSwap'

        if not amount:
            amount = await self.client.wallet.balance(token=from_token)
            if not amount.Wei:
                return f'{failed_text}: {self.client.account.address} | SyncSwap | swap_token | ' \
                       f'not enough {from_token_name} balance ({amount.Ether})'

        contract = await self.client.contracts.get(contract_address=Contracts.SYNC_SWAP)

        if not from_token_is_eth:
            if await self.approve_interface(
                token_address=from_token.address,
                spender=contract.address,
                amount=amount
            ):
                await asyncio.sleep(random.randint(5, 10))
            else:
                return f'{failed_text} | can not approve'

        if from_token_name in ('BUSD', 'USDT'):
            from_token_price_dollar = 1
        else:
            from_token_price_dollar = await self.get_token_price(token_symbol=from_token_name)

        if to_token_name in ('BUSD', 'USDT'):
            to_token_price_dollar = 1
        else:
            to_token_price_dollar = await self.get_token_price(token_symbol=to_token_name)

        amount_out_min = TokenAmount(
            amount=float(amount.Ether) * from_token_price_dollar / to_token_price_dollar * (100 - slippage) / 100,
            decimals=await self.client.transactions.get_decimals(contract=to_token)
        )

        params = TxArgs(
            paths=[
                TxArgs(
                    steps=[
                        TxArgs(
                            pool=pool.address,
                            data=f'0x{from_token.address[2:].zfill(64)}'
                                 f'{str(self.client.account.address)[2:].zfill(64)}'
                                 f'{("2" if from_token_is_eth else "1").zfill(64)}',
                            callback='0x0000000000000000000000000000000000000000',
                            callbackData='0x'
                        ).tuple()

                    ],
                    tokenIn='0x0000000000000000000000000000000000000000' if from_token_is_eth else from_token.address,
                    amountIn=amount.Wei
                ).tuple()
            ],
            amountOutMin=amount_out_min.Wei,
            deadline=int(time.time() + 20 * 60)
        )

        tx_params = TxParams(
            to=contract.address,
            data=contract.encodeABI('swap', args=params.tuple()),
            value=amount.Wei if from_token_is_eth else 0
        )

        # self.parse_params(tx_params['data'])
        # return

        tx_params = await self.client.transactions.auto_add_params(tx_params)
        return (await self.client.transactions.estimate_gas(tx_params)).Wei

        tx = await self.client.transactions.sign_and_send(tx_params=tx_params)
        receipt = await tx.wait_for_receipt(client=self.client, timeout=300)
        if receipt:
            return f'{amount.Ether} {from_token_name} was swapped to {to_token_name} via SyncSwap: {tx.hash.hex()}'
        return f'{failed_text}!'

    async def swap_eth_to_usdc(self, amount: TokenAmount | None = None, slippage: float = 1.) -> str:
        return await self._swap(
            from_token=Contracts.WETH,
            to_token=Contracts.USDC,
            pool=Contracts.SYNCSWAP_ETH_USDC_POOL,
            amount=amount,
            slippage=slippage
        )

    async def swap_eth_to_usdt(self, amount: TokenAmount | None = None, slippage: float = 1.) -> str:
        return await self._swap(
            from_token=Contracts.WETH,
            to_token=Contracts.USDT,
            pool=Contracts.SYNCSWAP_ETH_USDT_POOL,
            amount=amount,
            slippage=slippage
        )

    async def swap_eth_to_busd(self, amount: TokenAmount | None = None, slippage: float = 1.5) -> str:
        return await self._swap(
            from_token=Contracts.WETH,
            to_token=Contracts.ceBUSD,
            pool=Contracts.SYNCSWAP_ETH_BUSD_POOL,
            amount=amount,
            slippage=slippage
        )

    async def swap_eth_to_wbtc(self, amount: TokenAmount | None = None, slippage: float = 1) -> str:
        return await self._swap(
            from_token=Contracts.WETH,
            to_token=Contracts.WBTC,
            pool=Contracts.SYNCSWAP_ETH_WBTC_POOL,
            amount=amount,
            slippage=slippage
        )

    async def swap_usdc_to_eth(self, amount: TokenAmount | None = None, slippage: float = 1) -> str:
        return await self._swap(
            from_token=Contracts.USDC,
            to_token=Contracts.WETH,
            pool=Contracts.SYNCSWAP_ETH_USDC_POOL,
            amount=amount,
            slippage=slippage
        )

    async def swap_usdt_to_eth(self, amount: TokenAmount | None = None, slippage: float = 1) -> str:
        return await self._swap(
            from_token=Contracts.USDT,
            to_token=Contracts.WETH,
            pool=Contracts.SYNCSWAP_ETH_USDT_POOL,
            amount=amount,
            slippage=slippage
        )

    async def swap_busd_to_eth(self, amount: TokenAmount | None = None, slippage: float = 1) -> str:
        return await self._swap(
            from_token=Contracts.ceBUSD,
            to_token=Contracts.WETH,
            pool=Contracts.SYNCSWAP_ETH_BUSD_POOL,
            amount=amount,
            slippage=slippage
        )

    async def swap_wbtc_to_eth(self, amount: TokenAmount | None = None, slippage: float = 1) -> str:
        return await self._swap(
            from_token=Contracts.WBTC,
            to_token=Contracts.WETH,
            pool=Contracts.SYNCSWAP_ETH_WBTC_POOL,
            amount=amount,
            slippage=slippage
        )