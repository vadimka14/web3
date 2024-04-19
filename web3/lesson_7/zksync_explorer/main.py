import asyncio
# from zksync_explorer.explorer_api import get_txs_explorer, APIFunctions
# from zksync_explorer import config
from explorer_api import get_txs_explorer, APIFunctions
import config


async def main():

    api_oklink = APIFunctions(url='https://www.oklink.com', key=config.OKLINK_API_KEY)
    # print(
    #     await get_txs_explorer(
    #         account_address='C'
    #     )
    # )
    # res = (
    #     await get_txs_explorer(
    #         account_address='0x32400084C286CF3E17e7B677ea9583e60a000324'
    #     ))['items']
    # for r in res:
    #     print(r)
    # res = await api_oklink.account.txlist(address='0x32400084C286CF3E17e7B677ea9583e60a000324')
    # print(res)
    res = await api_oklink.account.find_tx_by_method_id(
        address='0x7131b37478af63e775402248583099974a005b75',
        to='0x7131b37478af63e775402248583099974a005b75',
        method_id='0xeb672419'
    )

    # for r in res:
    for r in res.items():
        print(r)
    print(len(res))


asyncio.run(main())