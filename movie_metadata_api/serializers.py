from rest_framework import serializers
from . import models


class Actor(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = '__all__'


class MovieList(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = ['id', 'title']


class MovieRetrieve(serializers.ModelSerializer):
    actors = Actor(read_only=True, many=True)

    class Meta:
        model = models.Movie
        fields = "__all__"


class MovieEditCreate(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"



