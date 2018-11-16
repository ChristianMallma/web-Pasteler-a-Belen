from django.contrib import admin
from .models import design

#Extendemos clase de administración
class designAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Registramos modelo en el administrador
admin.site.register(design, designAdmin)

