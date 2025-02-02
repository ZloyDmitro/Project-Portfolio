"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Portfolio import views
from .views import ContactView

urlpatterns = [
    path('', views.home, name='index'),
    path('contact/', views.contact_form, name='contact_form'),
    path('contact_form/', views.contact_form, name='contact_form_endpoint'),
    path('api/contact/', ContactView.as_view(), name='contact_api'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('resume/download_pdf/', views.download_pdf, name='download_pdf'),
]



