from rest_framework import generics 
from rest_framework.filters import SearchFilter
from book.models import Book
from book.serializers import BookSerializer
from rest_framework import permissions

class BookSearchView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'author']