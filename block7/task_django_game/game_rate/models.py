from django.db import models

from game.models import Game
from user.models import User


class GameRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rate = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}, {self.game}, {self.rate}'
