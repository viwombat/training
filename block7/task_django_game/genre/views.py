from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from genre.models import Genre
from genre.serializer import GenreSerializer


@api_view(['GET', 'POST'])
def genres_list(request):
    if request.method == 'GET':
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def genres_details(request, pk=None):
    if request.method == 'GET':
        queryset = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(queryset)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        try:
            game = Genre.objects.get(pk=pk)
            game.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
