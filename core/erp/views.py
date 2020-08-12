from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from core.erp.models import Servicio,Blog,Presentacion
from core.erp.forms import FormularioContacto
# Create your views here.
def Servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios.html',{"servicios": servicios })

def Home(request):
    pre = Presentacion.objects.all()
    return render(request, 'home.html',{"presentacion": pre})

def BlogView(request):
    if request.method == 'POST':
        print('Se envio el correo')
    blogs = Blog.objects.all()
    return render(request, 'blog.html',{"blogs": blogs })

def Contacto(request):
    if request.method == "POST":
        miFormu = FormularioContacto(request.POST)
        if miFormu.is_valid():
            infForm = miFormu.cleaned_data
            send_mail(infForm['mail'],infForm['mensaje'],infForm.get("mail",""),['ernesto.alom@rolloseimpresiones.com'],)
            return render(request,"gracias.html")
    else:
        miFormu = FormularioContacto()

    return render(request,"contacto.html", {"form":miFormu})
