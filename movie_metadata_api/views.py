from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from . import models
from . import serializers


class DefaultPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        response_schema = {
            'meta': {
                'count': self.page.paginator.count,
                'page_size': self.page_size,
                'page': self.page.number,
                'last_mage': self.page.end_index()
            },
            'data': data
        }
        return Response(response_schema)


class Movies(mixins.CreateModelMixin,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.ListModelMixin,
            GenericViewSet):

    pagination_class = DefaultPagination
    queryset = models.Movie.objects.get_queryset().order_by('id')

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.MovieList
        elif self.action == 'retrieve':
            return serializers.MovieRetrieve
        else:
            return serializers.MovieEditCreate


class Actors(viewsets.ModelViewSet):
    pagination_class = DefaultPagination
    queryset = models.Actor.objects.get_queryset().order_by('id')
    serializer_class = serializers.Actor