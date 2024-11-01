from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from books_app.filters import BookFilter
from books_app.models import Book
from books_app.pagination import BookListPagination
from books_app.permissions import IsAdminOrReadOnly
from books_app.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookListPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
