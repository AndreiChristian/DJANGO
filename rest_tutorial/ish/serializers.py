from rest_framework import serializers
from ish.models import FacilityItem

class FacilityItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityItem
        fields = "__all__"
