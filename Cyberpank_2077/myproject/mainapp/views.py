from django.shortcuts import render

# Create your views here.

def index(request):
    templates = 'mainapp/index.html'
    return render(request, templates)

def about(request):
    templates = 'mainapp/about.html'
    return render(request, templates)

def contacts(request):
    templates = 'mainapp/contacts.html'
    return render(request, templates)