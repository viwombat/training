from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from game.models import Game
from publisher.serializer import PublisherSerializer


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    price = serializers.FloatField()
    release_date = serializers.DateField()
    publisher = PublisherSerializer()

    def create(self, validated_data):
        publisher_data = validated_data.pop('publisher')
        publisher_serializer = PublisherSerializer(data=publisher_data)
        if publisher_serializer.is_valid():
            publisher = publisher_serializer.save()
            game = Game.objects.create(publisher=publisher, **validated_data)
            return game
        else:
            raise serializers.ValidationError("Error creating game")

    def update(self, instance, validated_data):
        publisher_data = validated_data.pop('publisher')
        publisher_serializer = PublisherSerializer(instance.publisher, data=publisher_data)

        if publisher_serializer.is_valid():
            publisher = publisher_serializer.save()
            instance.name = validated_data.get('name', instance.name)
            instance.price = validated_data.get('price', instance.price)
            instance.release_date = validated_data.get('release date', instance.release_date)
            instance.publisher = publisher
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("Error updating game")
