import mmh3

import requests


response = requests.get('url/favicon.ico', verify=False)

favicon = response.content.encode('base64')

hash = mmh3.hash(favicon)

print(hash)
