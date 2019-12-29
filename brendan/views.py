from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.template.loader import get_template


class HomePageView(TemplateView):
    template_name = 'home.html'


class ServicesPageView(TemplateView):
    template_name = 'services.html'

# Fuction based view


def emailview(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['brendangaturudevelopers@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "contact.html", {'form': form})

# def emailview(request):
#     if request.method == "POST":
#         # form = ContactForm(request.POST)
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")
#         subject = "Contact Form Received"
#         from_email = email
#         to_email = "brendangaturudevelopers@gmail.com"
#
#         context = {
#             'user': name,
#             'email': email,
#             'message': message
#         }
#         contact_message = get_template('contact_message.txt').render(context)
#
#         send_mail(subject, contact_message, from_email, to_email)
#         return redirect("home")
#     return render(request, "contact.html", {})
