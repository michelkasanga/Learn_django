from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Author, Book
from .forms import BookForm
from time import sleep


"""
   SELECT  : all(), get()
   WHERE  : get_object_or_404()
   FILTER  : filter()
               __gte = supérieur ou égal
               __lte = inférieur ou égal
               __gt = supérieur
               __lt = inférieur
               __exact = égal
               __contains = contient
               __icontains = contient (insensible à la casse)
               __startswith = commence par
               __istartswith = commence par (insensible à la casse)
               __endswith = se termine par
               __iendswith = se termine par (insensible à la casse)
               __range = entre deux valeurs
               __in = dans une liste de valeurs
               __isnull = est nul ou non nul
               
   DISTINCT  : distinct() 
   AGGREGATE  : aggregate()
   EXCLUDE  : exclude()
   ORDER BY : order_by()
   LIMIT  : [:n] (not used here)
   INSERT  : create()
   UPDATE  : save() = modifier un objet existant en faisant un get() puis un save()
   UPDATE  : update() = modifier un ou plusieurs objets en faisant un filter() puis un update()
   SELECT COUNT(*)  : count()
   DELETE  : delete()
   MAnyToMany :  
   
"""
def is_visitor(user):
   return user.groups.filter(name='visiteur').exists()

def index(request):
   context = {"books": Book.objects.all}
   return render(request,"mangalib/index.html", context)

@user_passes_test(is_visitor)
def show(request, book_id):
      context = {'book':get_object_or_404(Book, pk=book_id)}
      return render(request,"mangalib/show.html", context)
 

@permission_required('mangalib.add_book', raise_exception= True)
def add(request):
   if request.method == 'POST':
      form = BookForm(request.POST)
      
      if form.is_valid():
         form.save()
         return redirect('mangalib:index')
   else:
      form = BookForm()
   return render(request,"mangalib/book_form.html", {'form':form, 'nom':'Ajout'})

@permission_required('mangalib.change_book', raise_exception= True)
def edit(request, book_id):
   book = Book.objects.get(pk=book_id)
   if request.method == 'POST':
      form = BookForm(request.POST, instance = book)
      
      if form.is_valid():
         form.save()
         return redirect('mangalib:index')
   else:
      form = BookForm(instance=book)
   return render(request,"mangalib/book_form.html", {'form':form, 'nom':'Ajout'})

def remove(request, book_id):
   if not request.user.has_perm('mangalib.delete_book'):
       return HttpResponse(f"<span style=\"color:red;\" >Vous n\'avez pas le droit de supprimer ce livre.</span>", status=403)
      
   book = Book.objects.get(pk=book_id)
   book.delete()
   return redirect('mangalib:index')



   """                                                                    
   liste  de decorators pour les vues
   @login_required : nécessite une connexion pour accéder à la vue
   @permission_required : nécessite un droit spécifique pour accéder à la vue
   @user_passes_test : nécessite que la fonction de test retourne True pour accéder à la vue
   @csrf_exempt : désactive la protection CSRF pour la vue
   @require_http_methods : nécessite que la requête soit de type GET, POST, PUT, DELETE, etc.
   @require_POST : nécessite que la requête soit de type POST
   @require_GET : nécessite que la requête soit de type GET
   @require_safe : nécessite que la requête soit de type GET ou HEAD
   @cache_page : met en cache la vue pour une durée spécifiée
  user.has_perm('mangalib.add_book') : vérifie si l'utilisateur a le droit d'ajouter un livre
  user.all().exists() : vérifie si l'utilisateur a au moins un droi

   """