from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"),
]
#observación: el category_id, se pasará como parámetro auntomáticamente en la vista
#             recordar también, que ese parámetro siempre es cadena de caracteres, 
#             por eso lo casteamos a entero(int)