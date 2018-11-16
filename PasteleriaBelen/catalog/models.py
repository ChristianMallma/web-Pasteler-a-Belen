from django.db import models

# Creando modelo para subir los diseños
class design(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(verbose_name='Descripción')
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    image = models.ImageField(upload_to='catalog')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Catálogo de producto'
        verbose_name_plural = 'Catálogo de productos'
        ordering = ['-created']

    def __str__(self):
        return self.name
    
