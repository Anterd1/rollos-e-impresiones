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


class Blog(models.Model):
    title_post = models.CharField(max_length=70)
    content = models.TextField()
    image = models.ImageField(upload_to='blog')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.title_post

class Presentacion(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    created = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name= 'presentacion'

    def __str__(self):
        return self.title