from rest_framework import serializers
from .models import Property, FacilityCategory, FacilityItem, FacilitySubCategory


class FacilityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityItem
        fields = ['id', 'name','subcategory']


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
