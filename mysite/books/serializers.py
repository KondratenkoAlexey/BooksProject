from rest_framework import serializers
from .models import Book, Author


class BooksSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    published = serializers.CharField(max_length=5)
    # authors = serializers.CharField(max_length=200)
    # image = serializers.ImageField()
    pages = serializers.IntegerField()
    rating = serializers.FloatField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.published = validated_data.get('published', instance.published)
# authors and image
        instance.pages = validated_data.get('pages', instance.pages)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance


class AuthorsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    surname = serializers.CharField(max_length=50)
    # books = serializers.CharField()

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.save()
        return instance