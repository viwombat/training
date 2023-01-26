from django.db import models


class Publisher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Game(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    release_date = models.DateField()
    # publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    age = models.IntegerField()
    # games = models.ManyToManyField(Game, on_delete=models.CASCADE)


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    # games = models.ManyToManyField(Game, on_delete=models.CASCADE)
