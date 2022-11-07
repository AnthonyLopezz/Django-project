from django.shortcuts import render, redirect
from .forms.forms import FormContact
from django.core.mail import EmailMessage, send_mail


# Create your views here.


def contact(request):
    context = {
        'form_contact': FormContact()
    }
    if request.method == "POST":
        form_contact = FormContact(data=request.POST)
        if form_contact.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")

            mail = EmailMessage("Message from Alterna Shop.",
                                "The user with name: {} with the email address {} "
                                "write the following:\n\n {}".format(name, email, message), "",
                                ["projectconst2021@gmail.com"], reply_to=[email])
            try:
                mail.send()
                return redirect("/contact/?valid")
            except (RuntimeError, TypeError, NameError):
                return redirect("/contact/?invalid")

    return render(request, "contact/contact.html", context)
