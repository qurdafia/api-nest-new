from django.conf.urls import url, include
from django.urls import path, include
from .views import EventsView
from rest_framework.routers import DefaultRouter


#router = DefaultRouter()
#router.register("events", EventsView, basename="events")
# router.register("attributes", AttributesViewSet, basename="attributes")


urlpatterns = [
    # path('', views.EventsView.as_view(),
         name='event')
    #url('', include(router.urls))
]
