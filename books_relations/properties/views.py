from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Property, FacilityCategory, FacilitySubCategory, FacilityItem, Reservation
from .serializers import PropertySerializer, FacilityCategorySerializer, FacilitySubCategorySerializer, FacilityItemSerializer, UserSerializer, ReservationSerializer
from django.contrib.auth.models import User


class PropertyListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class FacilityCategoryListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FacilityCategory.objects.all()
    serializer_class = FacilityCategorySerializer


class FacilityCategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FacilityCategory.objects.all()
    serializer_class = FacilityCategorySerializer


class FacilitySubCategoryListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FacilitySubCategory.objects.all()
    serializer_class = FacilitySubCategorySerializer


class FacilitySubCategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FacilitySubCategory.objects.all()
    serializer_class = FacilitySubCategorySerializer


class FacilityItemListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FacilityItem.objects.all()
    serializer_class = FacilityItemSerializer


class FacilityItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FacilityItem.objects.all()
    serializer_class = FacilityItemSerializer


class UserListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ReservationListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
