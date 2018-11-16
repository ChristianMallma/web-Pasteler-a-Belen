from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Creamos aquí nuestras pruebas
#Creamos prueba para saber si se ha creado un perfil al crear un usuario
class ProfileTestCase(TestCase):
    #método para preparar la prueba
    def setUp(self):
        #creamos usuario de prueba
        User.objects.create_user('test', 'test@test.com', 'test1234')#username, mail, contraseña
    
    #método para la prueba en sí
    def test_profile_exists(self):
        #comprobar si existe un usuario llamado test
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True) #comprobando que exists tenga el valor de True


#Observación:
#Ejecutamos el test, mediante la línea de comandos:
#python manage.py test registration