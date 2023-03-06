from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, viewsets

from user.models import User
from user.serializer import UserSerializer
from game.models import Game


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    permission_classes = (IsAuthenticated, )


class UserInfoViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        game_names = [game.name for game in Game.objects.filter(user=user)]
        user_data = UserSerializer(user).data

        response_data = {
            'user': user_data,
            'games': game_names
        }
        return Response(response_data, status=status.HTTP_200_OK)

    permission_classes = (IsAuthenticated, )
