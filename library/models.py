from datetime import date
from django.utils import timezone
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Author(models.Model):
    name=models.CharField(max_length=50)
    birth_date=models.DateField()
    biography=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    title =models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.CASCADE,related_name='book_author')
    publication_date=models.DateTimeField(default=timezone.now)
    price=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='review_book')
    reviewer_name= models.CharField(max_length=50)
    content =models.TextField(max_length=1000)
    rating_choices = [(i, str(i)) for i in range(6)]  # Choices from 0 to 5
    rating = models.IntegerField(choices=rating_choices, default=0)

    def __str__(self):
        return self.reviewer_name

