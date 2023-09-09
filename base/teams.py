import requests

# Roster API Request
rosterurl = "https://statsapi.mlb.com"
endpoint = "/api/v1/teams?sportId=1"

def main_request(rosterurl, endpoint):
    response = requests.get(rosterurl + endpoint)
    return response.json()

def parse_json(response):
    # charList = []
    for item in response['teams']:
        return
    #     char = {
    #         "id": item['person']["id"],
    #         "Full Name": item['person']['fullName'],
    #         "Position": item['position']['abbreviation']
    #     }
    #     charList.append(char)
    # return charList

teamsData = main_request(rosterurl, endpoint)
print(parse_json(teamsData))