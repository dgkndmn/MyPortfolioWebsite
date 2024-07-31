from django.shortcuts import render

# Create your views here.

def view_mainpage(request):
    return render(request, 'base.html')

def view_contact(request):
    return render(request, 'websiteapp/contact.html')

def view_aboutme(request):
    return render(request, 'websiteapp/aboutme.html')