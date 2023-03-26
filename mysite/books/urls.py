from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('api/v1/bookslist/', BooksAPIView.as_view()),
    path('api/v1/bookslist/<int:pk>/', BooksAPIDetailView.as_view()),
    path('api/v1/authorslist/', AuthorsAPIView.as_view()),
    path('api/v1/authorslist/<int:pk>/', AuthorsAPIDetailView.as_view()),
]