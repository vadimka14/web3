# import requests
# from fake_useragent  import UserAgent
# import json
# headers = {
#     'authority': 'interface.gateway.uniswap.org',
#     'accept': '*/*',
#     'accept-language': 'uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6,nl;q=0.5',
#     'content-type': 'text/plain;charset=UTF-8',
#     'origin': 'https://app.uniswap.org',
#     'referer': 'https://app.uniswap.org/',
#     'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-site',
#     'user-agent': UserAgent().random,
#     'x-request-source': 'uniswap-web',
# }
#
# data = {
#     "tokenInChainId": 10,
#     "tokenIn": "ETH",
#     "tokenOutChainId": 10,
#     "tokenOut": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
#     "amount": "100000000000000",
#     "sendPortionEnabled": True,
#     "type": "EXACT_INPUT",
#     "intent": "quote",
#     "configs": [
#         {
#             "protocols": ["V2", "V3", "MIXED"],
#             "enableUniversalRouter": True,
#             "routingType": "CLASSIC",
#             "recipient": "0x7131b37478af63e775402248583099974a005b75",
#             "enableFeeOnTransferFeeFetching": True
#         }
#     ]
# }
#
# response = requests.post('https://interface.gateway.uniswap.org/v2/quote', headers=headers, data=json.dumps(data))
# #print(response.status_code)
# #print(response.content)
# #print(response.text)
# print(int(response.json()['quote']['route'][0][0]['amountOut']) / 10 ** 6)