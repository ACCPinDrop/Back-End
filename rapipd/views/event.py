from rapipd.models import Event
from rapipd.serializers import EventSerializer

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination


class SetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20




class event_list(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ['event_name', 'event_group__group_name']
    ordering_fields  = '__all__'
    pagination_class = SetPagination

