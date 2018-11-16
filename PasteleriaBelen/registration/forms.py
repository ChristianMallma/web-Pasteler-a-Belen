from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

#Creando clase para el formulario de creación
class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    #Redefinimos la clase Meta, para extender el email
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    #Necesitamos validar que el usuario sea único para cada usuario (no se repita)
    def clean_email(self):  
        email = self.cleaned_data.get('email') #recuperando el email
        if User.objects.filter(email=email).exists(): #si email ya existe
            raise forms.ValidationError("El email ya está registrado, prueba con otro")
        return email

#Creando nuestro propio formulario para el perfil
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control mt-3', 'rows':3, 'placeholder':'Biografía'}),
            'link': forms.URLInput(attrs={'class':'form-control mt-3', 'placeholder':'Enlace'}),
        }

#Clase para nuestro formulario del email
class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ['email']
    
    #Necesitamos validar el email, después de cambiarlo
    def clean_email(self):  
        email = self.cleaned_data.get('email') #recuperando el email
        if 'email' in self.changed_data: #El email debe haber cambiado
            if User.objects.filter(email=email).exists(): #email no debe de existir en la base de datos
                raise forms.ValidationError("El email ya está registrado, prueba con otro")
        return email