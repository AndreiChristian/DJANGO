from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ish.models import FacilityItem, FacilityGroup
from ish.serializers import FacilityItemSerializer, FacilityGroupSerializer


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


@api_view(['GET', 'PUT', 'DELETE'])
def facility_item_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        facilityItem = FacilityItem.objects.get(pk=pk)
    except facilityItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacilityItemSerializer(facilityItem)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FacilityItemSerializer(facilityItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        FacilityItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def facility_group_list(request):
    if request.method == 'GET':
        facility_groups = FacilityGroup.objects.all()
        serializer = FacilityGroupSerializer(facility_groups, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description')
        item_ids = request.data.get('facility_items', [])

        if not name or not description or not item_ids:
            # Ensure that all required fields are provided
            return Response({'error': 'Missing required form data'}, status=status.HTTP_400_BAD_REQUEST)

        facility_items = FacilityItem.objects.filter(id__in=item_ids)
        facility_group = FacilityGroup.objects.create(
            name=name,
            description=description
        )
        facility_group.facility_items.set(facility_items)
        facility_group.save()

        serializer = FacilityGroupSerializer(facility_group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
