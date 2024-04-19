import csv
import requests
from bs4 import BeautifulSoup as BS
from fake_useragent import FakeUserAgent
from datetime import datetime
import time

csv_path = 'table.csv'
url = 'https://www.Benzinga.com/markets'


while True:
    links = []
    rows = [['Time', 'Header', 'Text', 'Link']]
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            links.append(row[3])
            rows.append(row)

    headers = {
        'user-agent': FakeUserAgent().random
    }




    response = requests.get(url, headers=headers)
        # with open('text.html', 'w') as f:
    #     f.write(response.text)
    html = BS(response.content, 'html.parser')
    news_lst = html.select('.newsfeed-card.text-black')

    for  i, news in enumerate(news_lst, start=1):
        link = news.get('href')
        header = news.select('span div span')[0].text.strip()
        text = news.select('span.post-teaser')[0].text.strip().replace('\n', ' ').replace('\t', '')
        if link in links:
            continue
        rows.append([str(datetime.now()), header, text, link])

    with open('table.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    time.sleep(30)