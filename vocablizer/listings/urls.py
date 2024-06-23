from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('my_flashcards/', views.my_flashcards, name='my_flashcards'),
]
