from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Actor", unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255)
    length = models.PositiveIntegerField(null=True, default=None)
    actors = models.ManyToManyField(Actor, related_name='movies', verbose_name="Actors")

    def __str__(self):
        return self.title
