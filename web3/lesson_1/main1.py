from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account.signers.local import LocalAccount
from data.config import pk, seed
from eth_async.utils import utils


eth_rpc = 'https://eth.llamarpc.com'
arb_rpc = 'https://arbitrum.llamarpc.com'


def get_private_from_seed(seed: str) -> str:
    web3 = Web3(provider=Web3.HTTPProvider(endpoint_uri=arb_rpc))
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)
    web3.eth.account.enable_unaudited_hdwallet_features()

    web3_account: LocalAccount = web3.eth.account.from_mnemonic(seed)

    private_key = web3_account._private_key.hex()
    address = web3_account.address
    return private_key


web3 = Web3(Web3.HTTPProvider(endpoint_uri=arb_rpc))
print(web3.is_connected())

print(f'Gas price: {web3.eth.gas_price} WEI')

address = web3.eth.account.from_key(private_key=pk).address
wallet_address = Web3.to_checksum_address(address)
print(wallet_address)
balance = web3.eth.get_balance(wallet_address)
print(balance)
ether_balance = Web3.from_wei(balance, 'ether')
print(ether_balance)
# balance = 111431411343410000
#
# ether_balance = Web3.from_wei(balance, 'ether')
# wei_balance = Web3.to_wei(ether_balance, 'ether')
# print(ether_balance)
# print(wei_balance)

private_key = get_private_from_seed(seed=seed)
print('private_key', private_key)

from eth_async.models import DefaultABIs
usdc_contract_address = Web3.to_checksum_address('0xaf88d065e77c8cc2239327c5edb3a432268e5831')
token_abi = utils.read_json('data/abis/token.json')
usdc_contract = web3.eth.contract(address=usdc_contract_address, abi=DefaultABIs.Token)
print(usdc_contract.functions.symbol().call())
print(usdc_contract.functions.decimals().call())
# print(usdc_contract.functions.balanceOf(wallet_address).call())
decimals = usdc_contract.functions.decimals().call()
print(usdc_contract.functions.balanceOf(wallet_address).call() / 18 ** decimals)