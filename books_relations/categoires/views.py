from rest_framework import generics, status
from .models import Category, Subcategory
from .serializers import CategoryOverviewSerializer, SubcategoryOverviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["GET", "POST"])
def categories_list(request):

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategoryOverviewSerializer(categories, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CategoryOverviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["GET", "POST"])
# def category_list(request):

#     if request.method == "GET":
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
