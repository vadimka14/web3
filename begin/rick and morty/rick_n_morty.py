import requests
from fake_useragent import FakeUserAgent
import os

main_dir = 'images'
main_page_dir = os.path.join(main_dir, 'main_page')
episodes_dir = os.path.join(main_dir, 'episodes')


#function download picture

def download_img(url: str, path: str):
    response_data = requests.get(url)
    with open(path, 'wb') as f:
        f.write(response_data.content)

headers = {
    'authority': 'rickandmortyapi.com',
    'accept': '*/*',
    'accept-language': 'uk-UA,uk;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://rickandmortyapi.com',
    'referer': 'https://rickandmortyapi.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': FakeUserAgent().random,
}

json_data = {
    'query': '\n    query randomCharacters($ids: [ID!]!) {\n      charactersByIds(ids: $ids) {\n        id\n        name\n        status\n        species\n        image\n        episode {\n          name\n          id\n        }\n        location {\n          name\n          id\n        }\n      }\n    }\n  ',
    'variables': {
        'ids': [
            675,
            57,
            163,
            423,
            29,
            487,
        ],
    },
}

response = requests.post('https://rickandmortyapi.com/graphql', headers=headers, json=json_data)
json_data = response.json().get('data', {}).get('charactersByIds', {})

#задача 1
# for elem in json_data:
#     img_src = elem['image']
#     filename = os.path.join(main_page_dir, img_src.split('/')[-1])
#     response = requests.get(img_src)
#
#     with open(filename, 'wb') as f:
#         f.write(response.content)

# дістать епізоди
episodes_ids = []
for elem in json_data:
    episode_lst = elem['episode']
    for episode in episode_lst:
        episodes_ids.append(episode['id'])
episodes_ids = list(set(episodes_ids))  #['8', '22', '18', '11', '28', '42']

episode_url = 'https://rickandmortyapi.com/api/episode/'

for episode_id in episodes_ids:
    character_urls = []

  #ctvoryt dir
    episodes_tmp_dir = os.path.join(episodes_dir, episode_id)
    os.mkdir(episodes_tmp_dir)

  #distat char

    response = requests.get(f'{episode_url}{episode_id}')
    json_episode_data = response.json()
    #print(json_episode_data)
    for character_url in json_episode_data['characters']:
        character_urls.append(character_url)

    for character_url in character_urls:
        # dsitat picture
        response = requests.get(character_url)
        print(response.json())
        image_src = response.json()['image']
        filename = os.path.join(episodes_tmp_dir, image_src.split('/')[-1])
        download_img(url=image_src, path=filename)

