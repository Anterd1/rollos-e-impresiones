from django.contrib import admin
from core.erp.models import Servicio, Blog,Presentacion
# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Blog)
admin.site.register(Presentacion)