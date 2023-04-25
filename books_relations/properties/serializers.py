from rest_framework import serializers
from django.core.mail import send_mail

from .models import Property, FacilityCategory, FacilityItem, FacilitySubCategory, Reservation
from django.contrib.auth.models import User


class FacilityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityItem
        fields = ['id', 'name', 'subcategory']


class FacilitySubCategorySerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        queryset=FacilityItem.objects.all(), many=True)

    class Meta:
        model = FacilitySubCategory
        fields = ['id', 'name', 'items', 'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = FacilityItemSerializer(
            instance.items.all(), many=True).data
        return representation


class FacilityCategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(
        queryset=FacilitySubCategory.objects.all(), many=True)

    class Meta:
        model = FacilityCategory
        fields = ['id', 'name', 'subcategories']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subcategories'] = FacilitySubCategorySerializer(
            instance.subcategories.all(), many=True).data
        return representation


class PropertySerializer(serializers.ModelSerializer):
    facility_categories = serializers.PrimaryKeyRelatedField(
        queryset=FacilityCategory.objects.all(), many=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'location',
                  'square_meters', 'facility_categories']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['facility_categories'] = FacilityCategorySerializer(
            instance.facility_categories.all(), many=True).data
        return representation


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class ReservationSerializer(serializers.ModelSerializer):
    property = serializers.PrimaryKeyRelatedField(
        queryset=Property.objects.all())
    users = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True)

    class Meta:
        model = Reservation
        fields = ['id', 'property', 'users', 'start_date', 'end_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['property'] = PropertySerializer(instance.property).data
        representation['users'] = UserSerializer(
            instance.users.all(), many=True).data
        return representation
