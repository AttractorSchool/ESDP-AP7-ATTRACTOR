from rest_framework import serializers

from cabinet_parents.models import City
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = (
            'author',
            'message',
            'response',
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
