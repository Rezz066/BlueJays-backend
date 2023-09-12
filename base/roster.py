import requests

# Roster API Request
rosterurl = "https://statsapi.mlb.com"
endpoint = "/api/v1/teams/141/roster"

def main_request(rosterurl, endpoint):
    response = requests.get(rosterurl + endpoint)
    return response.json()

def parse_json(response):
    charList = []
    for item in response['roster']:
        char = {
            "id": item['person']["id"],
            "Full Name": item['person']['fullName'],
            "Position": item['position']['abbreviation']
        }
        charList.append(char)
    return charList

rosterData = main_request(rosterurl, endpoint)
# print(parse_json(rosterData))