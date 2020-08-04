from django.urls import path

from core.erp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name="home"),
    path('servicios/',Servicios, name="servicios"),
    path('blog/',BlogView, name="blog"),
    path('contacto/',Contacto, name="contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)