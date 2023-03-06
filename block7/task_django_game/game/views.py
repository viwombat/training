from django.db.models import Avg, Prefetch
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status, viewsets

from game.models import Game
from game.serializer import GameSerializer
from game_rate.models import GameRate


class IsAdminOr403(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_staff:
            return True
        else:
            raise PermissionDenied('Error 403 - Not admin error')


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

    permission_classes = (IsAdminOr403, )


class PublisherGamesRateViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        avg_rate = GameRate.objects.filter(game__publisher__pk=pk).aggregate(Avg('rate'))

        response_data = {
            'avg_rate': avg_rate
        }

        return Response(response_data, status=status.HTTP_200_OK)

    permission_classes = (IsAdminOr403,)


class UsersAvgAgeViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        avg_age = GameRate.objects.prefetch_related('user', 'game')\
            .filter(game__publisher__pk=pk).aggregate(Avg('user__age'))

        response_data = {
            'avg_age': avg_age.values()
        }

        return Response(response_data, status=status.HTTP_200_OK)

    permission_classes = (IsAdminOr403, )
