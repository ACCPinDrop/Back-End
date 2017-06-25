from rapipd.models import Event
from rest_framework import viewsets
from rapipd.serializers import EventSerializer


class event_list(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
