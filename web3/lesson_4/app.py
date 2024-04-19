import asyncio

from eth_async.client import Client
from eth_async.models import Networks, TokenAmount

from tasks.mute import Mute
from tasks.space_fi import SpaceFi
from tasks.base import Base
from data.config import PRIVATE_KEY


async def main():
    client = Client(private_key=PRIVATE_KEY, network=Networks.Zksync)
    # base = Base(client=client)
    mute = Mute(client=client)
    space_fi = SpaceFi(client=client)
    # await base.get_token_info(contract_address='0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91')
    # await base.get_token_info(contract_address='0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4')
    # print(await mute.swap_eth_to_usdc(TokenAmount(amount=0.001)))

    print(await space_fi.swap_wbtc_to_eth())

if __name__ == '__main__':
    asyncio.run(main())
