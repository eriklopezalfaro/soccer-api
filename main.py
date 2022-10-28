import pprint as pp
import requests
import os, sys
from dotenv import load_dotenv

PLAYER = sys.argv[1]

def configure():
    load_dotenv()

def main():
    configure()

    url = "https://api-football-v1.p.rapidapi.com/v3/players"

    querystring = {"league":"61","search":PLAYER}

    headers = {
	    "X-RapidAPI-Key": os.getenv('api_key'),
	    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        sys.exit('TERMINATED')

    response = response.json()
    for res in response['response']:
        pp.pprint(res, indent=3)

    print(len(response['response']))

if __name__ == '__main__':
    main()