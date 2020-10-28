from django.conf.urls import url, include
from .views import EventsViewSet, AttributesViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("events", EventsViewSet, basename="events")
router.register("attributes", AttributesViewSet, basename="attributes")


urlpatterns = [
    url('', include(router.urls))
]
