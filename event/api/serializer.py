from rest_framework import serializers
from event.models import Attributes, Events


class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = ['id', 'conf', 'value', 'key']


class EventsSerializer(serializers.ModelSerializer):
    attributes = AttributesSerializer(many=True)

    class Meta:
        model = Events
        fields = ['id', 'deviceId', 'deviceName', 'personId', 'personName', 'attributes']
        depth = 1
