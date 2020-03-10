from rest_framework import serializers
from .models import Workers
# создаем сериализайзер для отображение данных в списки питон

class WorkersSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    surname = serializers.CharField(max_length=255)
    date_of_birth = serializers.IntegerField()
    position = serializers.CharField(max_length=255)

    def create(self, validated_data): # метод для сообщение инструкции при вызове метода "save"
        return Workers.objects.create(**validated_data)