import asyncio

from py_okx_async.OKXClient import OKXClient

from config import okx_credentials
from okx_actions import OKXActions
from py_okx_async.models import OKXCredentials, Chains, AccountTypes


async def main():
    okx_client = OKXClient(credentials=okx_credentials)

    # subaccounts_lst = await okx_client.subaccount.list()
    # for subaccount_name in subaccounts_lst:
    #     print(subaccount_name)
    #     print(await okx_client.subaccount.asset_balances(subAcct=subaccount_name, token_symbol='ETH'))
    # print()

    # print(await okx_client.subaccount.asset_balances(subAcct='BASHKA'))
    # currencies = await okx_client.asset.currencies()
    # for currency in currencies.keys():
    #     print(currency)
    #     for network in currencies[currency]:
    #         print(f'{network}|', end='')
    #     print()
    # print(await okx_client.asset.balances())
    # deposits = await okx_client.asset.deposit_history()
    # for key, value in deposits.items():
    #     print(f'{key}: {value}')
    # for balance in balances:
    #     print(balance)
    # withdrawals = await okx_client.asset.withdrawal_history()
    # for key, value in withdrawals.items():
    #     print(f'{key}: {value}')


    okx_actions = OKXActions(credentials=okx_credentials)

    # print(await okx_actions.all_balances_are_zero())
    # print(await okx_actions.collect_funds_from_subaccounts())
    # print(await okx_actions.get_withdrawal_fee(token_symbol='ETH', chain=Chains.ArbitrumOne))
    # print(await okx_actions.try_to_get_tx_hash(wd_id=115902399))

if __name__ == '__main__':
    if okx_credentials.completely_filled():
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    else:
        print('Specify all variables in the .env file!')