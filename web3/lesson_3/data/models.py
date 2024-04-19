from eth_async.models import RawContract, DefaultABIs
from eth_async.utils.utils import read_json
from eth_async.classes import Singleton

from data.config import ABIS_DIR


class Contracts(Singleton):
    # Arbitrum
    ARBITRUM_WOOFI = RawContract(
        title="WooFi",
        address='0x9aed3a8896a85fe9a8cac52c9b402d092b629a30',
        abi=read_json(path=(ABIS_DIR, 'woofi.json'))
    )

    ARBITRUM_USDC = RawContract(
        title='USDC',
        address='0xaf88d065e77c8cC2239327C5EDb3A432268e5831',
        abi=DefaultABIs.Token
    )

    ARBITRUM_USDC_e = RawContract(
        title='USDC_e',
        address='0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8',
        abi=DefaultABIs.Token
    )

    ARBITRUM_ETH = RawContract(
        title='ETH',
        address='0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE',
        abi=DefaultABIs.Token
    )

    ARBITRUM_ARB = RawContract(
        title='ARB',
        address='0x912ce59144191c1204e64559fe8253a0e49e6548',
        abi=DefaultABIs.Token
    )

    ARBITRUM_WBTC = RawContract(
        title='WBTC',
        address='0x2f2a2543b76a4166549f7aab2e75bef0aefc5b0f',
        abi=DefaultABIs.Token
    )

    ARBITRUM_STARGATE = RawContract(
        title='arbitrum_stargate',
        address='0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614',
        abi=read_json(path=(ABIS_DIR, 'stargate.json'))
    )

    ARBITRUM_UNISWAP_ROUTER = RawContract(
        title='arbitrum_uniswap_router',
        address='0x5e325eda8064b456f4781070c0738d849c824258',
        abi=read_json(path=(ABIS_DIR, 'uniswap.json'))
    )

    ARBITRUM_GETH = RawContract(
        title='GETH',
        address='0xdD69DB25F6D620A7baD3023c5d32761D353D3De9',
        abi=DefaultABIs.Token
    )

    ARBITRUM_TESTNETBRIDGE = RawContract(
        title='arbitrum_testnetbridge',
        address='0xdd69db25f6d620a7bad3023c5d32761d353d3de9',
        abi=read_json(path=(ABIS_DIR, 'testnetbridge.json'))
    )

    POLYGON_STARGATE = RawContract(
        title='polygon_stargate',
        address='0x45A01E4e04F14f7A4a6702c74187c5F6222033cd',
        abi=read_json(path=(ABIS_DIR, 'stargate.json'))
    )

    POLYGON_USDC = RawContract(
        title='USDC',
        address='0x2791bca1f2de4661ed88a30c99a7a9449aa84174',
        abi=DefaultABIs.Token
    )

    AVALANCHE_STARGATE = RawContract(
        title='avalanche_stargate',
        address='0x45A01E4e04F14f7A4a6702c74187c5F6222033cd',
        abi=read_json(path=(ABIS_DIR, 'stargate.json'))
    )

    AVALANCHE_USDC = RawContract(
        title='USDC',
        address='0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e',
        abi=DefaultABIs.Token
    )

    OPTIMISM_STARGATE = RawContract(
        title='optimism_stargate',
        address='0xB0D502E938ed5f4df2E681fE6E419ff29631d62b',
        abi=read_json(path=(ABIS_DIR, 'stargate.json'))
    )

    OPTIMISM_USDC = RawContract(
        title='USDC',
        address='0x7f5c764cbc14f9669b88837ca1490cca17c31607',
        abi=DefaultABIs.Token
    )

    BSC_USDT = RawContract(
        title= 'USDT',
        address='0x55d398326f99059ff775485246999027b3197955',
        abi=DefaultABIs.Token
    )

    BSC_COREDAO_BRIDGE = RawContract(
        title='bsc_coredao_bridge',
        address='0x52e75d318cfb31f9a2edfa2dfee26b161255b233',
        abi=read_json(path=(ABIS_DIR, 'coredao_bridge.json'))
    )
