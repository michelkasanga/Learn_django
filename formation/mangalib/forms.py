from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset= Author.objects.all(), label='Auteur')
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity']
        labels = {'title': 'Titre', 'quantity':'Quantité'}
        
    # Méthode de validation personnalisée pour le champ 'quantity'
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity <= 0 or quantity > 100:
            raise forms.ValidationError("La quantité doit être comprise entre 1 et 100.")
        return quantity
    
    
    def clean(self):
        title = self.cleaned_data.get('title')
        quantity = self.cleaned_data.get('quantity')
        
        if title and quantity:
            if title.lower().startswith("one piece") and quantity < 10:
                raise forms.ValidationError("La quantité pour 'One Piece' doit être au moins 10.")
            
        return self.cleaned_data