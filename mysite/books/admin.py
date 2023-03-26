from django.contrib import admin
from .models import Book, Author


class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pages', 'rating')
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname')
    list_display_links = ('id', 'surname', 'name')
    search_fields = ('name', 'surname')


admin.site.register(Book, BooksAdmin)
admin.site.register(Author, AuthorAdmin)

