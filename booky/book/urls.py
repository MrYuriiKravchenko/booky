from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, GenreViewSet, AddCommentView, GetCommentsView, RatingViewSet, GetFrontendPageBooks, CommentDeleteView

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')
router.register('genre', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls)),
    path("get_frontendpage_books/",GetFrontendPageBooks.as_view()),
    path("comments/<slug:book_slug>/add/", AddCommentView.as_view()),
    path("comments/<slug:book_slug>/", GetCommentsView.as_view()),
    path("comments/<int:comment_id>/delete/", CommentDeleteView.as_view(), name='comment-delete'),
    path("books/<slug:book_pk>/ratings/", RatingViewSet.as_view({
        'get': 'list', 
        'post': 'create',
    }), name='book-ratings'),
    path("books/<slug:book_pk>/ratings/<int:pk>/", RatingViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='rating-detail'),
]
