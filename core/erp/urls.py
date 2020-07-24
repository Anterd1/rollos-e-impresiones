from django.urls import path

from core.erp.views import *

urlpatterns = [
    path('', Home, name="home"),
    path('servicios/',Servicios, name="servicios"),
    path('blog/',Blog, name="blog"),
    path('contacto/',Contacto, name="contacto"),
]