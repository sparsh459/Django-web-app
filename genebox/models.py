from pyexpat import model
from tkinter import CASCADE
from django.conf import settings
from django.db import models

# Create your models here.
class Authors(models.Model):
    Gender_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('Other', 'Others'),
    )
    Name = models.CharField(max_length=70)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20, choices=Gender_choice)
    Country = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.Name


class Books(models.Model):
    Name = models.CharField(max_length=250)
    Author = models.ForeignKey('Authors', on_delete=models.CASCADE, default=None)
    Published_Date = models.DateField(blank=False)
    Pages = models.IntegerField()
    critics = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.Name