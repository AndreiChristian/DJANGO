from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ish.models import FacilityItem, FacilityGroup, FacilityCategory
from ish.serializers import FacilityItemSerializer, FacilityGroupSerializer, FacilityCategorySerializer


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


@api_view(['GET', 'POST'])
def facility_group_list(request):
    if request.method == 'GET':
        facility_groups = FacilityGroup.objects.all()
        serializer = FacilityGroupSerializer(facility_groups, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacilityGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def facility_category_list(request):
    """
    List all facility categories, or create a new one.
    """
    if request.method == 'GET':
        faciliy_categories = FacilityCategory.objects.all()
        serializer = FacilityCategorySerializer(faciliy_categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacilityGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def facility_category_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        facility_category_detail = FacilityCategory.objects.get(pk=pk)
    except FacilityCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = FacilityCategorySerializer(facility_category_detail)
        return Response(serializer.data)

    # if request.method == "POST":
    #     serializer = FacilityCategorySerializer(
    #         facility_category_detail, data=request.data)
    #     if serializer.is_valid():
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        facility_category_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
