#Lo primero es registrarlo dentro de la librería de templates
from django import template
from pages.models import Page

#Pasos para registrar en la librería
register = template.Library()

@register.simple_tag  #decorador(transformamos una función normal en un tag, y lo registramos en la librería de templates)
def get_page_list():
    pages = Page.objects.all()
    return pages


