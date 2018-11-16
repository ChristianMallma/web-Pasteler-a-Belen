from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Creando vistas
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):#identificar o primary key
    category = get_object_or_404(Category, id=category_id) #para recoger un único registro
    return render(request, "blog/category.html", {'category':category})

#Observación: usamos get_object_or_404 en reemplazo de Category.objects.get()
#             para capturar el error