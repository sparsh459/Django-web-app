from django.conf import settings
from django.forms import DateField
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
    Published = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model= Books
        fields = '__all__'
        exclude = ['Author']