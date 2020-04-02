from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.template.loader import get_template


class HomePageView(TemplateView):
    template_name = 'home.html'


class WebdesignPageView(TemplateView):
    template_name = 'webdesign.html'


class WebdevelopmentPageView(TemplateView):
    template_name = 'webdesign.html'


class MobileDevelopmentPageView(TemplateView):
    template_name = 'mobiledevelopment.html'


class DigitalmarketingPageView(TemplateView):
    template_name = 'digitalmarketing.html'


class ContentwritingPageView(TemplateView):
    template_name = 'contentwriting.html'


class CreativedesignPageView(TemplateView):
    template_name = 'creativedesigns.html'




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
