from django.db import models
from account.models import User
from book.models import Book

class ReadingStatus(models.Model):
    STATUS_CHOICES = (
        ('want_to_read', 'Хочу прочитать'),
        ('reading', 'Читаю сейчас'),
        ('read', 'Прочитал'),
        ('not_finished', 'Не дочитал'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_statuses')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_statuses')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        unique_together = ('user', 'book')  

    def __str__(self):
        return f"{self.user} - {self.book} - {self.get_status_display()}"