from rest_framework import viewsets
from rest_framework.response import Response
from event.models import Events, Attributes
from .serializer import EventsSerializer, AttributesSerializer
from rest_framework.generics import ListAPIView, CreateAPIView


class EventsView(ListAPIView, CreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
