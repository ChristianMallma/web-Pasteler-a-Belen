from django.contrib import admin
from .models import Service

#Creando clase de extensión del administrador
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# Register your models here.
admin.site.register(Service, ServiceAdmin)
