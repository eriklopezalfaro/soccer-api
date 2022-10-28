import pprint as pp
import requests

url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"league":"61","search":"neymar"}

headers = {
	"X-RapidAPI-Key": "f1654be039mshb33692f6178cb18p1977bbjsnbd55a7260427",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()

for res in response['response']:
    pp.pprint(res, indent=3)