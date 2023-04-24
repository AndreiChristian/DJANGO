from rest_framework import serializers
from .models import Category, Book

# Category serializer

# Book serializer, including the related Category


class BookSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name','books']
