from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Servicio(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField( )
    image = models.ImageField(upload_to='servicios')
    created = models.DateField(auto_now_add=True)
    updated =  models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.title


