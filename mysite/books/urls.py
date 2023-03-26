from django.urls import path
from .views import index, BooksAPIView, AuthorsAPIView

urlpatterns = [
    path('', index),
    path('api/v1/bookslist/', BooksAPIView.as_view()),
    path('api/v1/bookslist/<int:pk>/', BooksAPIView.as_view()),
    path('api/v1/authorslist/', AuthorsAPIView.as_view()),
    path('api/v1/authorslist/<int:pk>/', AuthorsAPIView.as_view()),
]