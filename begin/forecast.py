import requests

city = input('Введіть місто:')


url = f'https://wttr.in/{city}?format=%t+%C'

response = requests.get(url)

print(f"Погода в городе {city}: {response.text}")