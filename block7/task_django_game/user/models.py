from django.db import models

from game.models import Game


class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    games = models.ManyToManyField(Game)
