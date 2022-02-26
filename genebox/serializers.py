from pyexpat import model
from attr import fields
from rest_framework import serializers
from genebox.models import Authors, Books

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['Name', 'Age', 'Gender', 'Country']
    # Name = serializers.CharField(max_length=70)
    # Age = serializers.IntegerField()
    # Gender = serializers.ChoiceField(choices=[('M','Male'),('F','Female'),('Other','Others')])
    # Country = serializers.CharField(max_length=70)

    # def create(self, validated_data):
    #     return Authors.create(validated_data)

    # def update(self, instance, validated_data):
    #     instance.Name = validated_data.get('Name', instance.Name)
    #     instance.Age = validated_data.get('Age', instance.Age)
    #     instance.Gender = validated_data.get('Gender', instance.Gender)
    #     instance.Country = validated_data.get('Country', instance.Country)
    #     instance.save()
    #     return instance

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['Name', 'Author', 'Published_Date', 'Pages', 'critics']
