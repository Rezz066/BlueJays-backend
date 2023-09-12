from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .roster import rosterData
from .teams import teamsData
from .players import playersData

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/rosters/',
        '/api/rosters/<id>/',

        '/api/rosters/upload/'

        '/api/rosters/<id>/display/',

        'api/rosters/delete/<id>/',
        'api/rosters/<update>/<id>/',

        'api/teams/',
        'api/teams/<id>',

        'api/players/',
        'api/players/<id>',
    ]
    return Response(routes)

@api_view(['GET'])
def getRosters(request):
    return Response(rosterData)


@api_view(['GET'])
def getRoster(request, id):
    result = None
    print("Searching for id:", id)
    print("Type of id:", type(id))
    for player_id in rosterData['roster']:
        print("player ID: ", player_id['person']['id'])
        print("Type of Player ID: ", type(player_id['person']['id']))
        if player_id['person']['id'] == id:
            print('Player ID after if statement: ', player_id['person']['id'])
            result = player_id
            break

    print("Result:", result)

    return Response(result)


@api_view(['GET'])
def getTeams(request):
    for team in teamsData['teams']:
        print(team['abbreviation'])
    return Response(teamsData)

@api_view(['GET'])
def getTeam(request, id):
    result = None
    print("Searching for id:", id)
    print("Type of id:", type(id))
    for team_id in teamsData['teams']:
        print("player ID: ",team_id['springLeague']['id'])
        if team_id['springLeague']['id'] == id:
            print('Player ID after if statement: ', team_id['springLeague']['id'])
            result = team_id
            break

    print("Result:", result)

    return Response(result)

@api_view(['GET'])
def getPlayers(request):
    return Response(playersData)


@api_view(['GET'])
def getPlayer(request, id):
    result = None
    print("Searching for id:", id)
    print("Type of id:", type(id))
    for player_id in playersData['roster']:
        print("player ID: ", player_id['person']['id'])
        print("Type of Player ID: ", type(player_id['person']['id']))
        if player_id['person']['id'] == id:
            print('Player ID after if statement: ', player_id['person']['id'])
            result = player_id
            break

    print("Result:", result)

    return Response(result)