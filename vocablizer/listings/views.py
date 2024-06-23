from django.shortcuts import render
from django.http import HttpResponse
from listings.models import English

def home(request):
    english_words = English.objects.all()
    return render(request, "listings/home.html",
                  {'words': english_words})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')