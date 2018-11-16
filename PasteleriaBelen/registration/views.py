from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

#Creamos vista de registro
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail #formulario que mostrará en esta vista
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    #Método para recuperar el formulario
    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificamos en tiempo real antes de recuperar el formulario
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Dirección email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Repita la contraseña'})
        return form

#Clase para poder editar el perfil de un usuario
@method_decorator(login_required, name='dispatch') #para que solo puedan actualizar perfil si está autenticado
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = "registration/profile_form.html"

    def get_object(self):
        #Recuperamos el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

#Clase para poder editar el email de un usuario
@method_decorator(login_required, name='dispatch') #para que solo puedan actualizar perfil si está autenticado
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = "registration/profile_email_form.html"

    def get_object(self):
        #Recuperamos el usuario
        return self.request.user
    
    #Modificamos el widget en tiempo de ejecución
    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        #Modificamos en tiempo real antes de recuperar el formulario
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form
