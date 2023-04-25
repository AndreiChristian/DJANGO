from rest_framework import serializers
from .models import Property, FacilityCategory, FacilityItem, FacilitySubCategory

class FacilityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityItem
        fields = ['id', 'name']

class FacilitySubCategorySerializer(serializers.ModelSerializer):
    items = FacilityItemSerializer(many=True, read_only=True)

    class Meta:
        model = FacilitySubCategory
        fields = ['id', 'name', 'items']

class FacilityCategorySerializer(serializers.ModelSerializer):
    subcategories = FacilitySubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = FacilityCategory
        fields = ['id', 'name', 'subcategories']

class PropertySerializer(serializers.ModelSerializer):
    facility_categories = serializers.PrimaryKeyRelatedField(queryset=FacilityCategory.objects.all(), many=True)

    class Meta:
        model = Property
        fields = ['id', 'name', 'location', 'square_meters', 'facility_categories']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['facility_categories'] = FacilityCategorySerializer(instance.facility_categories.all(), many=True).data
        return representation
