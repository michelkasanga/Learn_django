from django.db import models

"""
primary_key
unique
default
null
blank
choices


charfield
TextField
IntegerField
ForeignKey
DateTimeField
BooleanField
FileField
ImageField
emailField
URLField

"""
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    quantity = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
