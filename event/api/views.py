from rest_framework import viewsets
from rest_framework.response import Response
from event.models import Events, Attributes
from .serializer import EventsSerializer, AttributesSerializer


class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer

    def get_queryset(self):
        event = Events.objects.all()
        return event

    def create(self, request, *args, **kwargs):
        data = request.data

        new_event = Events.objects.create(
            deviceId=data["deviceId"], deviceName=data["deviceName"], personId=data["personId"], personName=data["personName"])

        new_event.save()

        # for attribute in data["attributes"]:
        #     attribute_obj = Attributes.objects.filter(id=id)
        #     new_event.attributes.add(attribute_obj)

        arr = data["attributes"]
        for x in arr:
            # attr_obj = Attributes.objects.filter(conf=x["conf"])
            print(x)
            new_event.attributes.add(x)

        serializer = EventsSerializer(new_event)

        return Response(serializer.data)


class AttributesViewSet(viewsets.ModelViewSet):
    serializer_class = AttributesSerializer

    def get_queryset(self):
        attribute = Attributes.objects.all()
        return attribute
