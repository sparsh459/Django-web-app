from django.contrib import admin
from django.urls import path
from genebox import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.AuthorList.as_view()),
    path('details/<str:pk>/', views.AuthorDetail.as_view()),
    path('books/', views.BookList.as_view()),
    path('Bdetails/<str:pk>/', views.BookDetail.as_view()),
    path('authorcsv/', views.author_csv, name='author_csv')
]