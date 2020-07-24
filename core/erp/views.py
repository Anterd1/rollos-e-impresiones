from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Servicios(request):
    return render(request, 'servicios.html')

def Blog(request):
    return render(request, 'blog.html')

def Contacto(request):
    return render(request, 'contacto.html')