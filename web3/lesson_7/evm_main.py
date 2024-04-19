import asyncio

from eth_async.client import Client
from eth_async.models import Networks


async def main():
    client = Client(network=Networks.Ethereum)

    address = '0x7131b37478af63e775402248583099974a005b75'

    # print(
    #     await client.network.api.functions.account.balance(address=address)
    # )
    # res = await client.transactions.find_txs(
    #     contract='0x32400084C286CF3E17e7B677ea9583e60a000324',
    #     function_name='requestL2Transaction',
    #     address=address,
    # )

    # for tx_hash, data in res.items():
    #     print(tx_hash, data)
    # res = (await client.network.api.functions.account.txlistinternal(
    #     address=address,
    # ))['result']
    # for r in res:
    #     print(r)
    #
    # res = (await client.network.api.functions.account.txlist(
    #     address=address,
    # ))['result']
    # for r in res:
    #     print(r)
    print(
        await client.network.api.functions.transaction.getstatus(txhash='0xc34b9b0857662ab4392939a7fa251eb001bd3a8dc2db0a9114159f6b863eb94c')
    )


asyncio.run(main())