from django.shortcuts import render
from django.http import HttpResponse
from listings.models import English
from django.shortcuts import get_object_or_404


def english_list(request):
    english_words = English.objects.all()
    return render(request, "listings/english_list.html",
                  {'words': english_words})

def english_detail(request, english_id):
    english_word = get_object_or_404(English, pk=english_id) # pk = primary key. Generate error404: generic error page
    return render(request, "listings/english_detail.html",
                  {'english_word': english_word})

def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')