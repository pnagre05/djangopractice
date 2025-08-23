#from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    #return HttpResponse("Welcome to the Home Page!")
    return render(request, 'home.html')

def aboutPage(request):
    #return HttpResponse("This is the About Page!")
    return render(request, 'about.html')