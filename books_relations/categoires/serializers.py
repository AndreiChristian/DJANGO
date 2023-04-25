from rest_framework import serializers
from categoires.models import Category, Subcategory


class CategoryOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class SubcategoryOverviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ["id", "name", "description", "category"]


class CategoryDetailSerializer(serializers.ModelSerializer):

    subcategories = SubcategoryOverviewSerializer(many="true", read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "description", "subcategories"]

    # def create_subcategory(self, instance, validated_data):
        
