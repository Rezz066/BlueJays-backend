from django.urls from path
from . import views

urlpattern = [
    path('', views.getRoutes, name="routes"),
]