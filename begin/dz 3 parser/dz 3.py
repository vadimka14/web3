import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import FakeUserAgent


headers = {
    'authority': 'www.spinxo.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'uk-UA,uk;q=0.9',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://www.spinxo.com',
    'referer': 'https://www.spinxo.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': FakeUserAgent().random,
    'x-requested-with': 'XMLHttpRequest',
}

json_data = {
    'snr': {
        'category': 0,
        'UserName': '',
        'Hobbies': '',
        'ThingsILike': '',
        'Numbers': '',
        'WhatAreYouLike': '',
        'Words': '',
        'Stub': 'username',
        'LanguageCode': 'en',
        'NamesLanguageID': '45',
        'Rhyming': False,
        'OneWord': False,
        'UseExactWords': False,
        'ScreenNameStyleString': 'Any',
        'GenderAny': False,
        'GenderMale': False,
        'GenderFemale': False,
    },
}

response = requests.post('https://www.spinxo.com/services/NameService.asmx/GetNames', headers=headers,  json=json_data)

names = []
while len(names) < 100:
    names += response.json().get('d', {}).get('Names', {})
    response = requests.post('https://www.spinxo.com/services/NameService.asmx/GetNames', headers=headers, json=json_data)

with open('name.txt', 'w') as f:
    for name in names:
        f.write(name + '\n')

