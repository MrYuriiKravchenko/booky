from rest_framework import viewsets, generics
from .serializers import GenreSerializer, BookSerializer, CommentSerializer, RatingSerializer
from .models import Book, Genre, Comment, Rating
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework import filters
from rest_framework.exceptions import ValidationError

class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 8
    page_query_param = 'page'
    ordering = 'title'

class BookViewSet(viewsets.ModelViewSet):
    search_fields = ['title', 'author']
    filter_backends = (filters.SearchFilter,)
    serializer_class = BookSerializer
    lookup_field = 'slug'
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination


    def get_queryset(self):
        queryset = Book.objects.all()
        genre_id = self.request.query_params.get('genre_id')

        if genre_id:
            queryset = queryset.filter(genre__id=genre_id)

        return queryset

class GetFrontendPageBooks(generics.ListAPIView):
    queryset = Book.objects.all()[0:4]
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]



class AddCommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentDeleteView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        username = request.user.username
        comment_id = self.kwargs.get('comment_id')
        comment = Comment.objects.get(id=comment_id)

        if comment.user.username == username:
            comment_text = comment.text
            comment.delete()
            return Response({
                "comment": comment_text,
                "message": "Comment успешно deleted",
            })
        else:
            return Response({
                "message": "У пользователя нет прав на удаление этого комментария",
            }, status=403)

class GetCommentsView(generics.ListAPIView):
    queryset = Comment.objects.all().order_by('-created')
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        book_slug = self.kwargs['book_slug'].lower()
        book = Book.objects.get(slug=book_slug)
        return Comment.objects.filter(book=book)
    
class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk' 


    def get_queryset(self):
        return Rating.objects.filter(book__slug=self.kwargs['book_pk'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user_id'] = self.request.user.id
        context['book_slug'] = self.kwargs['book_pk']
        return context 

    