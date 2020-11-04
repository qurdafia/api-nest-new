from rest_framework import serializers
from event.models import Attributes, Events
from drf_writable_nested.serializers import WritableNestedModelSerializer


class AttributesSerializer(WritableNestedModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Attributes
        fields = '__all__'


class EventsSerializer(WritableNestedModelSerializer):
    attributes = AttributesSerializer(many=True)

    class Meta:
        model = Events
        fields = ('id','deviceId', 'deviceName', 'idNumber', 'personName', 'attributes')
