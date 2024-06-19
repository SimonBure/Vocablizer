from django.shortcuts import render
from django.http import HttpResponse
from listings.models import English

def home(request):
    english_words = English.objects.all()
    return HttpResponse(f"""<h1>Home</h1>
    <p> This is a website to master any language you want. </p>
    <h2>English words:</h2>
    <ul>
        {[f'<li>{word.word}</li>' for word in english_words]}
    </ul>
                """)

def about(reqest):
    return HttpResponse('<h1>About</h1> <p> This is a website to master any language you want. </p>')

def contact(request):
    return HttpResponse('<h1>Contact</h1> <p> To be continued. </p>')