import os.path
import sys

from py_okx_async.models import OKXCredentials


if getattr(sys, 'frozen', False):
    ROOT_DIR = Path(sys.executable).parent.absolute()
else:
    ROOT_DIR = Path(__file__).parent.absolute()

ADDRESSES_PATH = os.path.join(ROOT_DIR, 'addresses.txt')

okx_api_key = '41356af3-0a72-4a7c-90b8-0a0e168a0898'
okx_secret_key = '32AB2AAB400B8D717DE3BE80CCA10BC9'
okx_passphrase = '&12324p4~425KT+5?iaAGndfj33333'

okx_credentials = OKXCredentials(
    api_key=okx_api_key,
    secret_key=okx_secret_key,
    passphrase=okx_passphrase
)

maximum_gas_price = 60
use_oficcial_bridge = False
withdraw_amount_to_eth = {'from': 0.0001, 'to': 0.0002}
withdraw_amount_to_zksync = {'from': 0.0001, 'to': 0.0002}
delay_between_withdrawals = {'from': 60, 'to': 120}
