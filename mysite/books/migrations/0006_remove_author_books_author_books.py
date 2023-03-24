# Generated by Django 4.0.6 on 2023-03-24 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_author_books_remove_book_authors_author_books_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(blank=True, to='books.book'),
        ),
    ]
