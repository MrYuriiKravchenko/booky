from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CurrentUserView, UserRegistrationView, UserProfileView

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-registrater'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('current_user/', CurrentUserView.as_view(), name='current_user'),
]