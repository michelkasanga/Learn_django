from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #chargeur de template
import datetime

def index(request):
   context = {
      'message': 'Salut Le Monde '.lower,
      'username':"Michel"
      }
   template = loader.get_template("mangalib/index.html")
   return HttpResponse(template.render(context, request))
 