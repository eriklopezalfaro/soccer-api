import requests
import pprint as pp

url = "https://api-football-v1.p.rapidapi.com/v3/leagues"

headers = {
	"X-RapidAPI-Key": "f1654be039mshb33692f6178cb18p1977bbjsnbd55a7260427",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()

# data = response['response'][0]
for res in response['response']:
    if response['response'].index(res) == 1:
        break
    data = res
    pp.pprint(data, depth=4, indent=4)