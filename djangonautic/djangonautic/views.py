from django.http  import HttpResponse
from django.shortcuts import render

def homepage(request):
   #return HttpResponse("About page")
   return render(request,'homepage.html')

def about(request):
    #return HttpResponse("HomePage") 
    return render(request,'about.html')
