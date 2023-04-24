from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Book, Category
from snippets.serializers import BookSerializer, CategorySerializer


@api_view(['GET', 'POST'])
def book_list(request, format=None):
    """
    List all books
    """
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request, format=None):

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk, format=None):

    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    if request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VERSION 1
# ____________________________________________________________________

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from snippets.models import Book
# from snippets.serializers import BookSerializer

# # Create your views here.


# @csrf_exempt
# def book_list(request):
#     """
#     List all the books and permit the creation of new ones
#     """
#     if request.method == "GET":
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def book_detail(request, pk):
#     """
#     Get the detail of one book, delete or update it!
#     """
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == "GET":
#         serializer = BookSerializer(book)
#         return JsonResponse(serializer.data)

#     if request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = BookSerializer(book, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     if request.method == "DELETE":
#         book.delete()
#         return HttpResponse(status=204)

