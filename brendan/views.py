from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class ServicesPageView(TemplateView):
    template_name = 'services.html'

# working on the contact view


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
                send_mail(name, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')
    return render(request, "contact.html", {'form': form})
