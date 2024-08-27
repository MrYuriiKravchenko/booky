from django.contrib import admin
from book.models import Genre, Book, Comment, Rating

class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'text', 'created']
    list_filter = ['created', 'user']

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class RatingAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating']
    list_filter = ['rating', 'user']

class RatingInLine(admin.TabularInline):
    model = Rating
    extra = 0

class GenreInline(admin.StackedInline): 
    model = Book.genre.through 
    extra = 1 # Количество пустых форм для добавления новых объектов

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    exclude = ('genre',)  # Исключить поле authors, так как мы будем работать через инлайн
    list_display = [
        'title', 'isbn', 'author', 'pub_date', 'language', 'slug', 'created'
        ]
    list_filter = ['title', 'author']
    search_fields = ['title', 'author']
    inlines = [CommentInLine, GenreInline, RatingInLine]

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}
    inlines = [GenreInline]

admin.site.register(Genre, GenreAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)