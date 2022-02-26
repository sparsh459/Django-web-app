from urllib import response
from django.http import HttpResponse, JsonResponse
from genebox.models import Authors, Books
from genebox.serializers import AuthorSerializer, BookSerializer
from rest_framework import generics
import csv

# Create your views here.

def home(request):
    return HttpResponse("home page")

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


class AuthorList(generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


# @api_view(['GET','POST'])
# def Author_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         authors = Authors.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         # checking if serializer is valid
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def Author_detail(request, pk):
#     """
#     Retrieve a snippet.
#     """
#     try:
#         author = Authors.objects.get(pk=pk)
#     except Authors.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data)
