from django.db import models

from game.models import Game


class Genre(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    games = models.ManyToManyField(Game)
