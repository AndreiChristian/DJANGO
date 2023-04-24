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
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop("books")
        category = Category.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(category=category, **book_data)
        return category

    # def create(self, validated_data):
    #     tracks_data = validated_data.pop('tracks')
    #     album = Album.objects.create(**validated_data)
    #     for track_data in tracks_data:
    #         Track.objects.create(album=album, **track_data)
    #     return album
