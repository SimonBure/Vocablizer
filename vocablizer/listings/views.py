from django.core.mail import send_mail
from listings.forms import ContactUsForm
from listings.models import English, EnglishForm, Example, ExampleForm
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def english_list(request):
    english_words = English.objects.all()
    return render(request,
                   "listings/english_list.html",
                  {'words': english_words})

def english_detail(request, english_id):
    english_word = get_object_or_404(English, pk=english_id) # pk = primary key. Generate error404: generic error page
    return render(request,
                   "listings/english_detail.html",
                  {'english_word': english_word})

def english_add(request):
    if request.method == 'POST':
        form = EnglishForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('english-list')
    else:
        form = EnglishForm()        
    return render(request,
                     "listings/english_add.html",
                     {'form': form})

def english_edit(request, english_id):
    english_word = get_object_or_404(English, pk=english_id)
    if request.method == 'POST':
        form = EnglishForm(request.POST, instance=english_word)
        if form.is_valid():
            form.save()
            return redirect('english-detail', english_word.id)
    else:
        form = EnglishForm(instance=english_word)
    return render(request,
                    "listings/english_edit.html",
                    {'form': form})

def example_add(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('example-list')
    else:
        form = ExampleForm()
    return render(request,
                   "listings/example_add.html",
                   {'form': form})

def example_list(request):
    examples = Example.objects.all()
    return render(request,
                   "listings/example_list.html",
                  {'examples': examples})

def example_detail(request, example_id):
    example = get_object_or_404(Example, pk=example_id) # pk = primary key. Generate error404: generic error page
    return render(request,
                   "listings/example_detail.html",
                  {'example': example})

def example_edit(request, example_id):
    example = get_object_or_404(Example, pk=example_id)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=example)
        if form.is_valid():
            form.save()
            return redirect('example-detail', example.id)
    else:
        form = ExampleForm(instance=example)
    return render(request,
                    "listings/example_edit.html",
                    {'form': form})

def about(request):
    return render(request,
                   'listings/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject='Website Inquiry : from ' + form.cleaned_data['email'],
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['calik63658@tiervio.com']
            )
        return redirect('email-sent')

    else:
        form = ContactUsForm()

    return render(request,
                    'listings/contact.html',
                {'form': form})

def email_sent(request):
    return render(request,
                   'listings/email_sent.html')