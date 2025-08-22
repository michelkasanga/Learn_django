from django.urls import path
from . import views

app_name = 'mangalib'

urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:book_id>/', views.show, name="show"),
    path('ajouter-libre/', views.add, name ='add'),
    path('modifier-livre/<int:book_id>/', views.edit, name='edit'),
    path('supprimer-livre/<int:book_id>/', views.remove, name='remove'),
    
]
 