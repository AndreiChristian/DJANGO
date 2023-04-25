from rest_framework import generics, status
from .models import Category, Subcategory
from .serializers import CategoryOverviewSerializer, SubcategoryOverviewSerializer, CategoryDetailSerializer
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


@api_view(["GET", "PUT", "POST", "DELETE"])
def categories_detail(request, pk):

    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # we are using Category Detail Serializer in order to get also the subcategories
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = CategoryOverviewSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "POST":
        print("this is the request data", request.data)
        Subcategory.objects.create(category=category,**request.data)
        return Response(status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
def subcategories_list(request):

    if request.method == "GET":
        categories = Subcategory.objects.all()
        serializer = SubcategoryOverviewSerializer(categories, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = SubcategoryOverviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET","PUT","POST","DELETE"])
def categories_detail(request):
    pass