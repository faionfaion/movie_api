from django.contrib import admin
from movie_metadata_api.models import Movie, Actor

admin.site.register(Actor)
admin.site.register(Movie)
