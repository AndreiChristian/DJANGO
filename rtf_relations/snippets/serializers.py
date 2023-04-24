from rest_framework import serializers
from snippets.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'size', 'price']


'''
this is the base version, using serializers.Serializer insted of serializers.ModelSerializer.
Therefore, fields are explicitily called and definied, as well as the create and update.
'''

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(read_only=True)
#     description = serializers.CharField()
#     size = serializers.IntegerField()
#     price = serializers.IntegerField()

#     def create(self, validated_data):
#         """
#         Create and return a news instance of a 'Book' model.
#         """
#         return Book.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title",instance.title)
#         instance.description = validated_data.get("description",instance.description)
#         instance.size = validated_data.get("size",instance.size)
#         instance.price = validated_data.get("price",instance.price)
#         instance.save()
#         return instance
