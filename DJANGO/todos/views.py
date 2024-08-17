from django.shortcuts import render
from django.http import HttpResponse 

def home(requeest):
    return render(requeest, "templates/home.html")
    
