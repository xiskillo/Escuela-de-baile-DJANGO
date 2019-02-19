from django.shortcuts import render,redirect
from .forms import ContactarForm
from django.urls import reverse
from django.core.mail import EmailMessage


# Create your views here.


def contactar(request):
    contactarForm=ContactarForm()
    
    if request.method == "POST":
                contactarForm=ContactarForm(data=request.POST)
                if contactarForm.is_valid:
                        nombre=request.POST.get('nombre', '')
                        email=request.POST.get('email', '')
                        mensaje=request.POST.get('mensaje', '')

                        
                       
                        email=EmailMessage("Mensaje Recibido en Escuela de Baile","Nombre:{}\nEMAIL:{}\n\n\nMensaje:\n{}".format(nombre,email,mensaje),
                                "xiskillo@inbox.mailtrap.io",["felixreyesf@gmail.com"],reply_to=[email])

                        email.send()
                        return redirect(reverse('contactar')+'?ok')
   
    
    return render(request, "contactar/contactar.html",{'form': contactarForm})