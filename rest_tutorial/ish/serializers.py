from rest_framework import serializers
from ish.models import FacilityItem, FacilityGroup

class FacilityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityItem
        fields = "__all__"

class FacilityGroupSerializer(serializers.ModelSerializer):

    facility_items = FacilityItemSerializer(many=True)
    class Meta:
        model = FacilityGroup
        fiels = "__all__"