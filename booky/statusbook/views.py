# status/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ReadingStatus
from .serializers import ReadingStatusSerializer

class ReadingStatusViewSet(viewsets.ModelViewSet):
    queryset = ReadingStatus.objects.all()
    serializer_class = ReadingStatusSerializer
    permission_classes = [IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
