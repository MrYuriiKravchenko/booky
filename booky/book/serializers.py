from rest_framework import serializers
from .models import Book, Genre, Comment, Rating
from account.models import User
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError

class GenreSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['id', 'name', 'slug', 'books']

    def get_books(self, obj):
        # Используем связь genre_books для получения всех книг, связанных с жанром
        books = obj.genre_books.all()
        return BookSerializer(books, many=True).data
        
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['rating']

    def create(self, validated_data):
        book_slug = self.context.get('book_slug')
        user_id = self.context.get('user_id')

        book = get_object_or_404(Book, slug=book_slug)

        rating, created = Rating.objects.get_or_create(
            book=book, 
            user_id=user_id, 
            defaults={'rating': validated_data['rating']}  
        )

        if not created:
            rating.rating = validated_data['rating']
            rating.save()
        
        return rating

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance


class BookSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Genre.objects.all())
    ratings = RatingSerializer(many=True)

    class Meta:
        model = Book 
        fields = ['id', 'description', 'title', 'isbn', 'author', 'pub_date', 'get_image', 'slug', 'language', 'ratings', 'genre', 'publishing_house']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    book = serializers.SlugRelatedField(slug_field="slug", queryset=Book.objects.all())

    class Meta:
        model = Comment 
        fields = ['id', 'title_text', 'text', 'created', 'user', 'book']
        


