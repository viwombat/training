from django.db.models import Avg
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, generics, viewsets

from publisher.models import Publisher
from publisher.serializer import PublisherSerializer
from game_rate.models import GameRate


class PublisherAPIView(GenericAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def get_queryset(self):
        return Publisher.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            publisher = self.get_object()
            serializer = self.get_serializer(publisher)
            return Response(serializer.data)
        else:
            publishers = self.get_queryset()
            serializer = self.get_serializer(publishers, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        publisher = self.get_object()
        publisher.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class PublisherGamesRateViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        avg_rate = GameRate.objects.filter(game__publisher__pk=pk).aggregate(Avg('rate'))

        response_data = {
            'avg_rate': avg_rate
        }

        return Response(response_data, status=status.HTTP_200_OK)
