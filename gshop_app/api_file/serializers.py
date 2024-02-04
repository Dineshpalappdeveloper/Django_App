from rest_framework import serializers
from ..models import CarList


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    is_active = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        return CarList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.is_active = validated_data.get(
            'is_active', instance.is_active)
        instance.save()
        return instance
