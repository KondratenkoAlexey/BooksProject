from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Book, Author
from .serializers import BooksSerializer, AuthorsSerializer


class BooksAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class BooksAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class AuthorsAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer


class AuthorsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer


def index(request):
    author = Author.objects.all()
    book = Book.objects.all()
    return render(request, 'index.html', {"author":author, 'book':book})
