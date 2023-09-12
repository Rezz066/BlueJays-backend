import requests

# Roster API Request
rosterurl = "https://statsapi.mlb.com"
endpoint = "/api/v1/teams?sportId=1"

def main_request(rosterurl, endpoint):
    response = requests.get(rosterurl + endpoint)
    return response.json()

def parse_json(response):
    for item in response['teams']:
        return

teamsData = main_request(rosterurl, endpoint)
print(parse_json(teamsData))