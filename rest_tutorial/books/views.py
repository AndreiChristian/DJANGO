from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book
from books.serializers import BookSerializer


@api_view(['GET', 'POST'])
def book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
