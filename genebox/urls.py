from django.contrib import admin
from django.urls import path
from genebox import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.Author_list, name='all_author'),
    path('authors/postform/', views.Author_list, name='authsave'),
    path('books/', views.Book_list, name='all_books'),
    path('books/postform/', views.Book_list, name='booksave'),
    path('authorcsv/', views.author_csv, name='author_csv'),
    path('bookcsv/', views.book_csv, name='book_csv'),
    path('authors/search/', views.search_author, name='searchauthor'),
    path('books/search/', views.search_book, name='searchbook')
]