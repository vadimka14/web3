import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.coingecko.com'
response = requests.get(url)


html = bs(response.content, 'html.parser')

print(html.select('.tw-border-y.tw-border-gray-200.tw-divide-y.tw-divide-gray-200.tw-w-full.sortable'))
# trs = table.select('tr')[1:]

# for tr in trs:
#     coin = tr.select('.tw-text-xs.tw-leading-4.tw-text-gray-500.tw-font-medium.tw-block')[0].text
#     print(coin)


#document.querySelector('.tw-border-y.tw-border-gray-200.tw-divide-y.tw-divide-gray-200.tw-w-full.sortable')
#.querySelectorAll('tr')[2].querySelector('.tw-text-xs.tw-leading-4.tw-text-gray-500.tw-font-medium.tw-block').innerText

#document.querySelector('.tw-divide-y.tw-divide-gray-200.tw-min-w-full')