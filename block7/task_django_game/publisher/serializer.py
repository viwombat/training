from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from publisher.models import Publisher


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    #
    # def create(self, validated_data):
    #     return Publisher.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance
