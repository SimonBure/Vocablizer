from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(reqest):
    return HttpResponse('<h1>About</h1> <p> This is a website to master any language you want. </p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p> To be continued. </p>')