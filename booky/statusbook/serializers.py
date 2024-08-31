# status/serializers.py

from rest_framework import serializers
from .models import ReadingStatus

class ReadingStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=ReadingStatus.STATUS_CHOICES, required=False, allow_blank=True)

    class Meta:
        model = ReadingStatus
        fields = ['id', 'user', 'book', 'status', 'created_at']
