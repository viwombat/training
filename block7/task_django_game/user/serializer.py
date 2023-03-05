from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from user.models import User
from game.serializer import GameSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    id = serializers.IntegerField()
    nickname = serializers.CharField(max_length=50)
    email = serializers.EmailField(allow_blank=False)
    age = serializers.IntegerField()
    game = GameSerializer(many=True)

    def create(self, validated_data):
        game_data = validated_data.pop('game')
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game = game_serializer.save()

            user = User.objects.create(game=game, **validated_data)
            return user
        else:
            raise serializers.ValidationError("Error creating user")

    def update(self, instance, validated_data):
        game_data = validated_data.pop('game')
        game_serializer = GameSerializer(instance.publisher, data=game_data)

        if game_serializer.is_valid():
            game = game_serializer.save()
            instance.nickname = validated_data.get('nickname', instance.nickname)
            instance.email = validated_data.get('email', instance.email)
            instance.age = validated_data.get('age', instance.age)
            instance.game = game
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("Error updating user")
