from django.db import models

from game.models import Game
from genre.models import Genre


class GameGenre(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game}, {self.genre}'
