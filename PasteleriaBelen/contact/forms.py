from django import forms

#Creando formulario
class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Escriba su nombre',
        }
    ), min_length=3, max_length=100)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Escriba su correo',
        }
    ), min_length=3, max_length=100)
    message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'rows':3,
            'placeholder':'Escriba su mensaje',
        }
    ), min_length=10, max_length=1000)






    #Observación: A diferencia de los modelos, para texto largo en formularios se usa
    #             CharField.