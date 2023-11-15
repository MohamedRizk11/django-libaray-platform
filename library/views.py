from django.shortcuts import render
from .models import Book ,Author

# Create your views here.

def book_list(request):
    all_books=Book.objects.all()
    return render(request,'library/book_list.html',{'books':all_books})


def book_detail(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,'library/book_detail.html',{'book':book})


def author_list(request):
    all_author=Author.objects.all()
    return render(request,'library/author_list.html',{'authors':all_author})


def author_detail(request,slug):
    author=Author.objects.get(slug=slug)
    return render(request,'library/author_detail.html',{'author':author})