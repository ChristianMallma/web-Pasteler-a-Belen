from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#definimos una función para guardar solo la imagen del avatar, más reciente
def custom_upload_to(instance, filename):#instance(objeto que se está guardando, filename es el fichero con la imagen que queremos sobreescribir)
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename #guarda el nuevo nombre dentro de profiles

# Creamos un modelo en la base de datos para el perfil de los usuarios
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #para conectar con los usuarios
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

#Tenemos que hacer que la función se llame automáticamente a través de un decorador
@receiver(post_save, sender=User) #(pre_save, post_save, pre_delete, post_delete) (y el modelo que tiene que enviar la señal)
#Función que se encarga de generar una instancia de perfil si es que esta no existe
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False): #si es la primera vez que se acaba de crear esta entrada
        Profile.objects.get_or_create(user=instance)
        print("Se acaba de crear un usuario y su perfil enlazado")


#Observación:
#para probar si se creo el perfil
#python manage.py shell
#from registration.models import Profile
#Profile.objects.get(user__username='pepito3')
#exit()