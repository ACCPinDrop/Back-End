from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets

from rapipd.models import Location
from rapipd.serializers import LocationsSerializer

class location_list(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationsSerializer


# @api_view(['GET', 'POST'])
# def location_list(request):
#     if request.method == 'GET':
# 	    locations = Location.objects.all()
# 	    serializer = LocationsSerializer(locations, many=True)
# 	    return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = LocationsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# @api_view(['GET', 'PUT', 'DELETE'])
# def location_detail(request, pk):
#     try:
#         location = Location.objects.get(pk=pk)
        
#     except Location.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = LocationsSerializer(location)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = LocationsSerializer(location, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)