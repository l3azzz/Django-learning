from django.http.response import HttpResponse
from django.shortcuts import render


def index(request): 
   name = "Basith"
   context = {
      "name": name
   }
   return render(request, "index.html", context=context)

def about(request):
   return render(request, "about.html")




