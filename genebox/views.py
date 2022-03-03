from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import render
from genebox.models import Authors, Books
from genebox.serializers import AuthorSerializer, BookSerializer
from genebox.filters import AutherFilter, BookFilter
import csv

# Create your views here.

def home(request):
    return render(request, 'base.html')

def author_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['content-dispositon'] = 'attachment; filename = authors.csv'

    # creatting csv writer
    writer = csv.writer(response)

    # designate th emodel
    authors = Authors.objects.all()

    #add column heading to csv file
    writer.writerow(['Author_Name', 'Age', 'Gender', 'Country'])

    # loop tru and output
    for author in authors:
        writer.writerow([author.Name, author.Age, author.Gender, author.Country])
    
    return response

def book_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['content-dispositon'] = 'attachment; filename = authors.csv'

    # creatting csv writer
    writer = csv.writer(response)

    # designate th emodel
    books = Books.objects.all()

    #add column heading to csv file
    writer.writerow(['Book_Name', 'Author', 'Published Date', 'Pages', 'Critics'])

    # loop tru and output
    for book in books:
        writer.writerow([book.Name, book.Author, book.Published, book.Pages, book.critics])
    
    return response


@api_view(['GET','POST'])
def Author_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    # calling the auther filter
    

    if request.method == 'GET':
        print('get')
        authors = Authors.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        
        # search filter data
        myFilter = AutherFilter(request.GET, queryset=authors)
        authors =  myFilter.qs
        
        context = {
            'author': authors,
            'myFilter':myFilter
        }
        # print(context)
        return render(request, 'author.html', context)

    elif request.method == 'POST':
        print('post')
        serializer = AuthorSerializer(data=request.data)
        # checking if serializer is valid
        if serializer.is_valid():
            serializer.save()
            return render(request, 'base.html')
        return HttpResponse("Bad Request")


@api_view(['GET','POST'])
def Book_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        authors = Books.objects.all()
        dbauthrs = Authors.objects.all()
        serializer = BookSerializer(authors, many=True)

        myFilter = BookFilter(request.GET, queryset=authors)
        authors =  myFilter.qs

        context = {
            'book':authors,
            'author':dbauthrs,
            'myFilter':myFilter
        }
        # print(context)
        return render(request, 'book.html', context)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        # checking if serializer is valid
        if serializer.is_valid():
            serializer.save()
            return render(request, 'base.html')
        return HttpResponse("bad request")

# def search_author(request):
#     query=request.GET['search']
#     authors = Authors.objects.filter(Name__icontains=query)
#     context = {
#             'author': authors
#         }
#     print(context)
#     return render(request, 'author.html', context)

# def search_book(request):
#     query=request.GET['search']
#     dbauthrs = Authors.objects.all()
#     authors = Books.objects.filter(Name__icontains=query)
#     context = {
#             'book':authors,
#             'author':dbauthrs
#         }
#     return render(request, 'book.html', context)