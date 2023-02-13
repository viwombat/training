from django.db import models

from game.models import Game
from user.models import User


# Create your models here.
class GameRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rate = models.IntegerField()
