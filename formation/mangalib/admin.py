from django.contrib import admin
from .models import Author, Book

"""
list_display: pour afficher les champs dans l'interface d'administration
list_editable: pour rendre certains champs modifiables directement dans la liste
search_fields: pour ajouter une barre de recherche
list_filter: pour filtrer les résultats
fields: pour définir les champs à afficher dans le formulaire d'édition
list_select_related: pour optimiser les requêtes liées
raw_id_fields: pour utiliser un champ de sélection simplifié pour les relations

ordering: pour définir l'ordre de tri par défaut
list_per_page: pour définir le nombre d'objets par page dans la liste
fieldsets: pour organiser les champs en sections dans le formulaire d'édition
list_display_links: pour rendre certains champs cliquables pour accéder à l'édition

"""

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Livre', {'fields': ('title', 'quantity',),}),
        ('Auteur', {'fields': ('author',),}),
        ]
    list_display = ('title', 'quantity', 'author') # Champs à afficher dans la liste
    list_filter = ('author',) # filtrer par auteur
    search_fields = ['title', 'author__name'] # Champs à rechercher
    ordering = ('title',) # Ordre de tri par titre
    list_per_page = 10 # Nombre d'objets par page
    list_editable = ('quantity',) # Champs modifiables directement dans la liste
    list_select_related = ('author',) # Optimiser les requêtes liées  
    list_display_links = ('title','author') # Rendre le titre cliquable pour accéder à l'édition
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

    
"""
    exemple de fielsets
    fieldsets = (
        ('Livre', { 'fields': ('title', 'quantity',)
        'description': 'Informations sur le livre',
        'classes': ('collapse',)  # pour rendre la section repliable
        }),
        ('Informations', { 'fields': ('author',)}),
    )
        '),
        ('Auteur', { 'fields': ('author',)}),
    )

"""