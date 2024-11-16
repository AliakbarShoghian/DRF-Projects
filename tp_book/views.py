from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from tp_book.models import Book
from tp_book.serializers import BookSerializer

# Create your views here.

# first API
"""class GettAPIView(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)"""


@api_view(['GET', 'POST'])
def book_view(request: Request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('id')
        book_serializer = BookSerializer(books, many=True)
        return Response(book_serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(None, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def book_detail_view(request: Request, book_id:int):
    try:
        book = Book.objects.get(id=book_id)
    except  Book.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        book.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
