from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from genre.models import Genre
from game.serializer import GameSerializer


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # game = GameSerializer()
    #
    # def create(self, validated_data):
    #     game_data = validated_data.pop('game')
    #     game_serializer = GameSerializer(data=game_data)
    #     if game_serializer.is_valid():
    #         game = game_serializer.save()
    #
    #         genre = Genre.objects.create(game=game, **validated_data)
    #         return genre
    #     else:
    #         raise serializers.ValidationError("Error creating genre")
    #
    # def update(self, instance, validated_data):
    #     game_data = validated_data.pop('game')
    #     game_serializer = GameSerializer(instance.publisher, data=game_data)
    #
    #     if game_serializer.is_valid():
    #         game = game_serializer.save()
    #         instance.name = validated_data.get('name', instance.name)
    #         instance.game = game
    #         instance.save()
    #         return instance
    #     else:
    #         raise serializers.ValidationError("Error updating genre")
