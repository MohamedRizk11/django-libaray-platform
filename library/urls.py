from django.urls import path
from .views import book_list,book_detail,author_list,author_detail
 

urlpatterns = [
    
    path('', book_list),
    path('/authors', author_list),
    path('<slug:slug>', book_detail), 
    path('<slug:slug>', author_detail),



]
