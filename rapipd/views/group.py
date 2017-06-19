from rapipd.models import Group
from rest_framework import viewsets
from rapipd.serializers import GroupSerializer


class group_list(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# @api_view(['GET', 'POST'])
# def group_list(request):
#     if request.method == 'GET':
# 	    groups = Group.objects.all()
# 	    serializer = GroupSerializer(groups, many=True)
# 	    return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = GroupSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# @api_view(['GET', 'PUT', 'DELETE'])
# def group_detail(request, pk):
#     try:
#         group = Group.objects.get(pk=pk)
        
#     except Group.DoesNotExist:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'GET':
#         serializer = GroupSerializer(group)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = GroupSerializer(group, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         group.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
