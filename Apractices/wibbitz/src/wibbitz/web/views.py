from django.shortcuts import render 


def index(request):
    # return render ( request,"<h1>hello</h1>") 
    return render ( request, "index.html")