from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm

class HomePageView(TemplateView):
    template_name = 'home.html'


class ServicesPageView(TemplateView):
    template_name = 'services.html'
