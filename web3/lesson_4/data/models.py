from eth_async.models import RawContract, DefaultABIs
from eth_async.utils.utils import read_json
from eth_async.classes import Singleton

from data.config import ABIS_DIR


class Contracts(Singleton):
    MUTE = RawContract(
        title='mute',
        address='0x8B791913eB07C32779a16750e3868aA8495F5964',
        abi=read_json(path=(ABIS_DIR, 'mute.json'))
    )

    SPACE_FI = RawContract(
        title='space_fi',
        address='0xbE7D1FD1f6748bbDefC4fbaCafBb11C6Fc506d1d',
        abi=read_json(path=(ABIS_DIR, 'space_fi.json'))
    )

    WETH = RawContract(
        title='WETH',
        address='0x5AEa5775959fBC2557Cc8789bC1bf90A239D9a91',
        abi=read_json(path=(ABIS_DIR, 'WETH.json'))
    )

    USDC = RawContract(
        title='USDC',
        address='0x3355df6D4c9C3035724Fd0e3914dE96A5a83aaf4',
        abi=DefaultABIs.Token
    )

    USDT = RawContract(
        title='USDT',
        address="0x493257fD37EDB34451f62EDf8D2a0C418852bA4C",
        abi=DefaultABIs.Token
    )

    WBTC = RawContract(
        title='WBTC',
        address='0xBBeB516fb02a01611cBBE0453Fe3c580D7281011',
        abi=DefaultABIs.Token
    )

    ceBUSD = RawContract(
        title='ceBUSD',
        address='0x2039bb4116b4efc145ec4f0e2ea75012d6c0f181',
        abi=DefaultABIs.Token
    )