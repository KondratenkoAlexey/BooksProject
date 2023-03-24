from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField('Book', blank=True)

    def __str__(self):
        return self.surname

    class Meta:
        ordering = ['id']


class Book(models.Model):
    title = models.CharField(max_length=150)
    published = models.IntegerField()
    authors = models.ManyToManyField('Author', blank=False)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    pages = models.IntegerField()
    rating = models.FloatField(max_length=5)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

