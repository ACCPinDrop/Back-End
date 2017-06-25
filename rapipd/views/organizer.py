from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from rapipd.models import Organizer
from rapipd.serializers import OrganizerSerializer

class organizer_list(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

