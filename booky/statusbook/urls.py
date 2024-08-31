from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReadingStatusViewSet  

router = DefaultRouter()
router.register('status', ReadingStatusViewSet, basename='status')  

urlpatterns = [
    path('', include(router.urls)),
]
