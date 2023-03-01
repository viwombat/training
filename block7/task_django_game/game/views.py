from django.db.models import Avg
from rest_framework.response import Response
from rest_framework import status, viewsets

from game.models import Game
from game.serializer import GameSerializer
from game_rate.models import GameRate
from user.models import User

from user.serializer import UserSerializer


class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Game.objects.all()
        serializer = GameSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PublisherGamesRateViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        games = Game.objects.filter(publisher__pk=pk)
        avg_rate = GameRate.objects.filter(game__in=games).aggregate(Avg('rate'))
        # games_data = [GameSerializer(game).data for game in games]

        response_data = {
            # 'games': games_data,
            'avg_rate': avg_rate
        }

        return Response(response_data, status=status.HTTP_200_OK)


class UsersAvgAgeViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        games = Game.objects.filter(publisher__pk=pk)
        users = GameRate.objects.filter(game__in=games).values('user')
        avg_age = User.objects.filter(id__in=users).aggregate(Avg('age'))

        response_data = {
            'avg_age': avg_age
        }

        return Response(response_data, status=status.HTTP_200_OK)
