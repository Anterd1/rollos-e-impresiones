from django.http import HttpResponse
from django.shortcuts import render

from core.erp.models import Servicio,Blog
# Create your views here.
def Home(request):
    servicios = Servicio.objects.all()
    return render(request, 'home.html',{"servicios": servicios })

def Servicios(request):
    return render(request, 'servicios.html')

def BlogView(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html',{"blogs": blogs })

def Contacto(request):
    return render(request, 'contacto.html')
