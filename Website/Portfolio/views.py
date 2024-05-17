from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, Http404
from django.conf import settings
import os



def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')

def resume(request):
    return render(request, 'resume.html')

# def contact_success(request):
#     return render(request, 'contact_success.html')


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if name and email and phone and message:  # Ensure no field is empty
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, 'Form submission successful! Thank you for reaching out.')
            return redirect('contact_form')
        else:
            # Handle missing form data
            messages.error(request, 'All fields are required.')
            return render(request, 'contact.html')
    return render(request, 'contact.html')



@method_decorator(csrf_exempt, name='dispatch')
class ContactView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

def download_pdf(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'Daniel_Resume.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404


