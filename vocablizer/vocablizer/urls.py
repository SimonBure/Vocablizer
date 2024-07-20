"""vocablizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('english/', views.english_list, name='english-list'),
    path('english/<int:english_id>/', views.english_detail, name='english-detail'),
    path('english/<int:english_id>/edit/', views.english_edit, name='english-edit'),
    path('english/<int:english_id>/delete/', views.english_delete, name='english-delete'),
    path('english/add/', views.english_add, name='english-add'),

    path('example/', views.example_list, name='example-list'),
    path('example/<int:example_id>/', views.example_detail, name='example-detail'),
    path('example/<int:example_id>/edit/', views.example_edit, name='example-edit'),    
    path('example/<int:example_id>/delete/', views.example_delete, name='example-delete'),
    path('example/add/', views.example_add, name='example-add'),

    path('about/', views.about, name='about'),

    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.email_sent, name='email-sent'),

]

