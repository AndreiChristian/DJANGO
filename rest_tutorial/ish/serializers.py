from rest_framework import serializers
from ish.models import FacilityItem, FacilityGroup, FacilityCategory


class FacilityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityItem
        fields = "__all__"


class FacilityGroupSerializer(serializers.ModelSerializer):

    facility_items = FacilityItemSerializer(many=True)

    class Meta:
        model = FacilityGroup
        fields = "__all__"


class FacilityCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FacilityCategory
        fields = "__all__"
