import requests

playerurl = "https://statsapi.mlb.com/"
endpoint = "api/v1/teams/141/roster/Active?hydrate=person(stats(type=season))"

def main_request(playerurl, endpoint):
    response = requests.get(playerurl + endpoint)
    return response.json()

def parse_json(response):
    for players in response['roster']:
        print(players)
    return players

playersData = main_request(playerurl, endpoint)