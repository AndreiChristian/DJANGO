from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ish.models import FacilityItem
from ish.serializers import FacilityItemSerializer


@api_view(['GET', 'POST'])
def facility_item_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        faciliy_items = FacilityItem.objects.all()
        serializer = FacilityItemSerializer(faciliy_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacilityItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
