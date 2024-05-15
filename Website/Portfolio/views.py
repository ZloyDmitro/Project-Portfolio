from django.shortcuts import render



def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')

def resume(request):
    return render(request, 'resume.html')


