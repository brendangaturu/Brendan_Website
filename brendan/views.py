from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ServicesPageView(TemplateView):
    template_name = 'services.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
