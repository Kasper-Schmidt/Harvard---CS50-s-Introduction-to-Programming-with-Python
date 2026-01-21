# Itunes bruger API til deres sange
# Dette søger efter sange, limit = antal, term bruges til at søge efter kunstner
# https://itunes.apple.com/search?entity=song&limit=3&term=eminem
# Downloader en JSON fil 

# python itunesAPI.py (kunstner navn)
# python itunesAPI.py eminem
# python itunesAPI.py travisscott

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2)) --> printer alt i json fil

# print kun sang navn
o = response.json()
for result in o["results"]:
    print(result["trackName"])




