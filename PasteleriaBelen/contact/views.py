from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Creando vistas de contacto (para email)
def contact(request):
    contact_form = ContactForm() #creando plantilla vacía
    
    #Procesamos el formulario solo cuando tenemos petición de tipo POST
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST) #rellenando plantilla con los campos automáticamente
        if contact_form.is_valid(): #si todos los campos estan rellenados o correctos
            #recuperando la información
            name = request.POST.get('name', '')
            email = request.POST.get('email','')
            message = request.POST.get('message','')
            #Enviamos correo y redireccionamos
            email = EmailMessage(
                "Pastelería Belen: Nuevo mensaje de contacto", #asunto
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, message), #cuerpo
                "no-contestar@inbox.mailtrap.io", #email_origen
                ["christian.mallma@unmsm.edu.pe"], #email_destino
                reply_to=[email],
            )
            try:
                email.send() #enviando mail
                #todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+'?ok')
            except:
                #algo ha fallado, redireccionamos a FAIL
                return redirect(reverse('contact')+'?fails')

    return render(request, "contact/contact.html", {'form':contact_form})

