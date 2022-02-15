from django.urls import path, include
from . import views
from rest_framework import routers

api_router = routers.SimpleRouter()
api_router.register('movies', views.Movies)
api_router.register('actors', views.Actors)

urlpatterns = [
    path('', include(api_router.urls)),
]