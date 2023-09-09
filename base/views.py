from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .roster import rosterData
from .teams import teamsData

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
    ]
    return Response(routes)

@api_view(['GET'])
def getRosters(request):
    return Response(rosterData)

@api_view(['GET'])
def getRoster(request, pk):
    roster = None

    for player in rosterData:
        if 'person' in player and 'id' in player['person']:
            player_id = player['person']['id']
            print(f"Checking player with id: {player_id}")
            # Check if player_id is a string and can be converted to an integer
            if isinstance(player_id, str) and player_id.isdigit():
                player_id = int(player_id)  # Convert the string to an integer
            # Now you can compare pk (an integer) with player_id (an integer)
            if isinstance(player_id, int) and player_id == pk:
                roster = player
                break
    
    if roster is not None:
        return Response(roster)
    else:
        return Response({'error': "Player not found"}, status=404)

# @api_view(['GET'])
# def getRoster(request, pk):
#     roster = None
#     for player in rosterData:
#         if 'person' in player and 'id' in player['person']:
#             if isinstance(player['person']['id'], int) and player['person']['id'] == pk:
#                 roster = player
#             break
#         if roster is not None:
#              return Response(roster)
#         else:
#             return Response({'error': "Player not found"}, status=404)
        
#     return Response(roster)

@api_view(['GET'])
def getTeams(request):
    return Response(teamsData)
