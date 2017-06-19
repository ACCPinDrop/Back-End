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

# @api_view(['GET', 'POST'])
# def organizer_list(request):
#     if request.method == 'GET':
# 	    organizers = Organizer.objects.all()
# 	    serializer = OrganizerSerializer(organizers, many=True)
# 	    return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrganizerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# @api_view(['GET', 'PUT', 'DELETE'])
# def organizer_detail(request, pk):
#     try:
#         organizer = Organizer.objects.get(pk=pk)
        
#     except Organizer.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = OrganizerSerializer(organizer)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = OrganizerSerializer(organizer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         organizer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)