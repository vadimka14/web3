# import requests
#
#
# url = 'https://chainid.network/chains.json'
# response = requests.get(url)
# data = response.json()
#
# for elem in data:
    # print(elem)
# for elem in data:
#     eip_1559 = False
#     if 'features' in elem and len(elem['features']):
#         for eip in elem['features']:
#             if eip['name'] == "EIP1559":
#                 eip_1559 = True
#     rpc = None
#     if len(elem['rpc']) != 0:
#         rpc = elem['rpc'][0]
#
#     explorers = None
#     if 'explorers' in elem and len(elem['explorers']):
#         explorers = elem['explorers'][0]['url']
#
#     ens = None
#     if 'ens' in elem and len(elem['ens']):
#         ens = elem['ens']['registry']
#
#     print(f"{elem['name']} | "
#           f"{elem['rpc']} | "
#           f"{elem['nativeCurrency']['name']} | "
#           f"{elem['nativeCurrency']['decimals']} | "
#           f"{elem['chainId']} | "
#           f"{elem['chain']} | "
#           f"{rpc} | "
#           f"EIP1559: {eip_1559} | "
#           f"explorer: {explorers} | "
#           f"ens: {ens}"
#           )
#"name | первое rpc | есть ли поддержка EIP1559 | название нативной монеты | decimals нативной монеты | chain id | ссылка на експлорер"

#{'name': 'Ethereum Mainnet',
# 'chain': 'ETH',
# 'icon': 'ethereum',
# 'rpc': ['https://mainnet.infura.io/v3/${INFURA_API_KEY}', 'wss://mainnet.infura.io/ws/v3/${INFURA_API_KEY}', 'https://api.mycryptoapi.com/eth', 'https://cloudflare-eth.com', 'https://ethereum.publicnode.com', 'wss://ethereum.publicnode.com', 'https://mainnet.gateway.tenderly.co', 'wss://mainnet.gateway.tenderly.co', 'https://rpc.blocknative.com/boost', 'https://rpc.flashbots.net', 'https://rpc.flashbots.net/fast', 'https://rpc.mevblocker.io', 'https://rpc.mevblocker.io/fast', 'https://rpc.mevblocker.io/noreverts', 'https://rpc.mevblocker.io/fullprivacy'],
# 'features': [{'name': 'EIP155'}, {'name': 'EIP1559'}],
# 'faucets': [],
# 'nativeCurrency': {'name': 'Ether', 'symbol': 'ETH', 'decimals': 18},
# 'infoURL': 'https://ethereum.org',
# 'shortName': 'eth',
# 'chainId': 1,
# 'networkId': 1,
# 'slip44': 60,
# 'ens': {'registry': '0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e'},
# 'explorers': [{'name': 'etherscan', 'url': 'https://etherscan.io', 'standard': 'EIP3091'}, {'name': 'blockscout', 'url': 'https://eth.blockscout.com', 'icon': 'blockscout', 'standard': 'EIP3091'}, {'name': 'dexguru', 'url': 'https://ethereum.dex.guru', 'icon': 'dexguru', 'standard': 'EIP3091'}]
# }

# Пользователь вводит chain_id и нужно вывести coin symbol (название нативной монеты в этой сети).
# Для получения информации использовать json словарь с сайта https://chainid.network/chains.json (с помощью requests)



# url = 'https://chainid.network/chains.json'
#
# response = requests.get(url)
# data = response.json()
#
# ask = int(input("Введіть chain id: "))
# for elem in data:
#     if elem['chainId'] == ask:
#         print(elem['nativeCurrency']['symbol'])
#         break


