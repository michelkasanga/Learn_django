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
ManyToManyField
DateTimeField
BooleanField
FileField
ImageField
emailField
URLField

"""
class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name= "Nom")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
    
class Book(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name="Titre")
    quantity = models.IntegerField(default=1, verbose_name="Quantité")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Auteur")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"