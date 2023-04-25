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
