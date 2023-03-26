from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Author
from .serializers import BooksSerializer, AuthorsSerializer


class BooksAPIView(APIView):
    def get(self, request):
        book = Book.objects.all()
        return Response({'books':BooksSerializer(book, many=True).data})

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'books':serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Book.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not allowed'})

        serializer = BooksSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'books': serializer.data})

class AuthorsAPIView(APIView):
    def get(self, request):
        author = Author.objects.all()
        return Response({'authors':AuthorsSerializer(author, many=True).data})

    def post(self, request):
        serializer = AuthorsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'authors':serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Author.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not allowed'})

        serializer = AuthorsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'authors': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Author.objects.get(pk=pk)
        except:
            return Response({'error': 'Method DELETE not allowed'})

        serializer = AuthorsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'authors': serializer.data})

def index(request):
    author = Author.objects.all()
    book = Book.objects.all()
    return render(request, 'index.html', {"author":author, 'book':book})
