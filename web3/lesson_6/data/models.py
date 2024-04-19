import os
from decimal import Decimal
from typing import Union
import json

from data.config import ABIS_DIR

ETH_ADDRESS = int('')
DAI_ADDRESS = int('')
USDC_ADDRESS = int('')
USDT_ADDRESS = int('')
MY_SWAP_TOKEN = int('')

DEFAULT_TOKEN_ABI = json.load(open(os.path.join(ABIS_DIR, 'default_token_ani.json')))


class TokenAmount:
    Wei: int
    Ether: Decimal
    decimals: int

    def __init__(self, amount: Union[int, float, str, Decimal], decimals: int = 18, wei: bool = False) -> None:
        """
        A token amount instance.
        :param Union[int, float, str, Decimal] amount: an amount
        :param int decimals: the decimals of the token (18)
        :param bool wei: the 'amount' is specified in Wei (False)
        """
        if wei:
            self.Wei: int = amount
            self.Ether: Decimal = Decimal(str(amount)) / 10 ** decimals

        else:
            self.Wei: int = int(Decimal(str(amount)) * 10 ** decimals)
            self.Ether: Decimal = Decimal(str(amount))

        self.decimals = decimals

    def __str__(self):
        return f'{self.Ether}'