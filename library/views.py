from django.shortcuts import render
from .models import Book

# Create your views here.

def book_list(request):
    all_books=Book.objects.all()
    return render(request,'library/book_list.html',{'books':all_books})


def book_detail(request,slug):
    book=Book.objects.get(slug=slug)
    return render(request,'library/book_detail.html',{'book':book})