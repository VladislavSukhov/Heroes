import requests
from pprint import pprint

# https://superheroapi.com/api/2619421814940190/search/Batman
hulk_url = "https://superheroapi.com/api/2619421814940190/search/Hulk"
captain_america_url = "https://superheroapi.com/api/2619421814940190/search/Captain_America"
batman_url = "https://superheroapi.com/api/2619421814940190/search/Batman"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
 
urls = [hulk_url, captain_america_url, batman_url]
heroes = []

for url in urls:
    resp = requests.get(url)
    resp_json = resp.json()
    id = resp_json["results"][0]["id"]
    name = resp_json["results"][0]["name"]
    intelligence = resp_json["results"][0]["powerstats"]["intelligence"]
    hero = (name, intelligence)
    heroes.append(hero)

heroes.sort(key = lambda x: x[1])
heroes.reverse()

pprint(f'Самый умный герой {heroes[0][0]}.')
