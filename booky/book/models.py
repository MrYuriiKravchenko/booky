from django.db import models
from account.models import User
from django.conf import settings



class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Genre'
        indexes= [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    author = models.CharField(max_length=200)
    images_book = models.ImageField(upload_to='uploads', null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='genre_books')
    pub_date = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=700)
    slug = models.SlugField()
    language = models.CharField(max_length=100)
    publishing_house = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def get_image(self):
        if self.images_book:
            return settings.WEBSITE_URL + self.images_book.url 
        else:
            return 'https://bulma.io/assets/images/placeholders/1280x960.png'

    
class Comment(models.Model):
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=700)
    title_text = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        # unique_together = ('user', 'book')
        ordering = ['-created']
        indexes = [
            models.Index(fields=['book']),
            models.Index(fields=['user']),
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'{self.user} - {self.book} - {self.text[:20]}'
    
class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')  
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_ratings') 
    rating = models.PositiveIntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'user') 

    def __str__(self):
        return f"{self.user}'s {self.rating}-star rating for {self.book}"