from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    #print("Tipo de petición: ", request.method)
    contactForm=ContactForm()
    if request.method == "POST":
        contactForm=ContactForm(data=request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name','')
            email=request.POST.get('email','')
            message=request.POST.get('message','')
            emailContact=EmailMessage(
                "La Cafetierra: Nuevo mensaje de contacto",
                "De {} <{}>\n\nMensaje:\n\n{}".format(name,email,message),
                "pmorales@itsqmet.edu.ec",
                ["correo-prueba@inbox.mailtrap.io"],
                reply_to=[email]            
            )
            try:
                emailContact.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

    return render(request ,"contact/contact.html", {'contactForm':contactForm})
