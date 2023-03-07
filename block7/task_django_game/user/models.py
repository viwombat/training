from django.db import models

from game.models import Game


class User(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    nickname = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=100)
    age = models.PositiveIntegerField()
    game = models.ManyToManyField(Game)

    def __str__(self):
        return self.nickname
