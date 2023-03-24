from rest_framework import serializers
from .models import Book, Author


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'published', 'image', 'pages', 'rating')


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'surname')
