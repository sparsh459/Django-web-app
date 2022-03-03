import django_filters
from django_filters import CharFilter
from genebox.models import Authors, Books


class AutherFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name')
    class Meta:
        model = Authors
        fields = '__all__'
        exclude = ['Country']

class BookFilter(django_filters.FilterSet):
    Name = CharFilter(field_name='Name')
    
    class Meta:
        model= Books
        fields = '__all__'
        exclude = ['Author']