import json
import requests
import sys


if len(sys.argv) != 2:
    sys.exit()

response = requests.get('https://itunes.apple.com/search?entity=musicVideo&limit=10&term=' + sys.argv[1])

obj = response.json()

for result in obj['results']:
    print(result)

# print(json.dumps(response.json(), indent=2))