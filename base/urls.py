from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('rosters/', views.getRosters, name="rosters"),
    path('rosters/<int:pk>', views.getRoster, name="roster"),
    path('teams/', views.getTeams, name="teams"),

]