from rest_framework import generics
from .models import Property, FacilityCategory, FacilitySubCategory, FacilityItem
from .serializers import PropertySerializer, FacilityCategorySerializer, FacilitySubCategorySerializer, FacilityItemSerializer

class PropertyListCreate(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class PropertyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class FacilityCategoryListCreate(generics.ListCreateAPIView):
    queryset = FacilityCategory.objects.all()
    serializer_class = FacilityCategorySerializer

class FacilityCategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FacilityCategory.objects.all()
    serializer_class = FacilityCategorySerializer

class FacilitySubCategoryListCreate(generics.ListCreateAPIView):
    queryset = FacilitySubCategory.objects.all()
    serializer_class = FacilitySubCategorySerializer

class FacilitySubCategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FacilitySubCategory.objects.all()
    serializer_class = FacilitySubCategorySerializer

class FacilityItemListCreate(generics.ListCreateAPIView):
    queryset = FacilityItem.objects.all()
    serializer_class = FacilityItemSerializer

class FacilityItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FacilityItem.objects.all()
    serializer_class = FacilityItemSerializer

