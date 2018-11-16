#Definimos el diccionario de contexto (para que se pueda usar en cualquier lugar del proyecto)

from .models import Link

def ctx_dict(request):
    ctx={}
    links = Link.objects.all()
    for link in links:
        ctx[link.key]=link.url #Para la clave key, muestra de valor a el url
    return ctx