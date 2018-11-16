from django.shortcuts import render
from .models import design

# Creando vistas
def product(request):
    designs = design.objects.all()
    return render(request, 'catalog/catalog.html', {'designs':designs})

