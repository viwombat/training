from django.db import models

from publisher.models import Publisher


class Game(models.Model):
    id = models.PositiveIntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    release_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)


