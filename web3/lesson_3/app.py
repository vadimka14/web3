import asyncio

from eth_async.client import Client
from eth_async.models import Networks, TokenAmount

from tasks.stargate import Stargate
from tasks.coredao import CoredaoBrigde
from tasks.uniswap import Uniswap
from tasks.testnetbridge import Testnetbridge
from data.config import PRIVATE_KEY


async def main():
    client = Client(private_key=PRIVATE_KEY, network=Networks.BSC)
    # stargate = Stargate(client=client)
    coredao_bridge = CoredaoBrigde(client=client)
    # uniswap = Uniswap(client=client)
    testnetbridge = Testnetbridge(client=client)

    # print((await stargate.get_network_with_usdc_balance(address=client.account.address)).name)
    res = await coredao_bridge.bridge_usdt_bsc_to_usdt_coredao(amount=TokenAmount(amount=0.01))
    print(res)
    # res = await uniswap.swap_eth_to_geth(amount_geth=TokenAmount(0.1), slippage=1)
    # print(res)
    #res = await testnetbridge.swap_geth(geth_amount=TokenAmount(0.01))
    #print(res)

if __name__ == '__main__':
    asyncio.run(main())
