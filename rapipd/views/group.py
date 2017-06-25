from rapipd.models import Group
from rest_framework import viewsets
from rapipd.serializers import GroupSerializer


class group_list(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

