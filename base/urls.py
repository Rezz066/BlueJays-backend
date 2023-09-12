from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('rosters/', views.getRosters, name="rosters"),
    path('rosters/<int:id>', views.getRoster, name="roster"),
    path('teams/', views.getTeams, name="teams"),
    path('teams/<int:id>', views.getTeam, name="team"),
    path('players/', views.getPlayers, name="players"),
    path('players/<int:id>', views.getPlayer, name="player"),
]