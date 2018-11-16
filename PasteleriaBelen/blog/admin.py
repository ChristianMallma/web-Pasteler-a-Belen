from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Tuneando el administrador
    list_display=('title', 'author', 'published', 'post_categories')
    #Que se ordenen por dos campos
    ordering = ('author', 'published')
    #Mostrando formulario de búsqueda
    search_fields=('title','content','author__username', 'categories__name')
    #Agregando jerarquía de fechas
    date_hierarchy='published'
    #Generando un campo de filtrado para búsqueda
    list_filter=('author__username', 'categories__name')

    #Método para poder mostrar categorías que tiene la entrada
    def post_categories(self, obj):
        #obj hace referencia a cada instancia o entrada
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    #sobreescribiendo un método para cambiar el nombre de la descripción
    post_categories.short_description='Categoría'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
