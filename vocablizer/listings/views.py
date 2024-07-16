from django.shortcuts import render
from listings.models import English
from listings.models import Example
from django.shortcuts import get_object_or_404

def english_list(request):
    english_words = English.objects.all()
    return render(request, "listings/english_list.html",
                  {'words': english_words})

def english_detail(request, english_id):
    english_word = get_object_or_404(English, pk=english_id) # pk = primary key. Generate error404: generic error page
    return render(request, "listings/english_detail.html",
                  {'english_word': english_word})

def example_list(request):
    examples = Example.objects.all()
    return render(request, "listings/example_list.html",
                  {'examples': examples})

def example_detail(request, example_id):
    example = get_object_or_404(Example, pk=example_id) # pk = primary key. Generate error404: generic error page
    return render(request, "listings/example_detail.html",
                  {'example': example})


def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')