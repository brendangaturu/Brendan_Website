from django.urls import path
from .views import HomePageView, ServicesPageView, WebdesignPageView, WebdevelopmentPageView, MobileDevelopmentPageView, DigitalmarketingPageView, ContentwritingPageView, CreativedesignPageView, emailview

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('webdesign/', WebdesignPageView.as_view(), name='webdesign'),
    path('webdevelopment/', WebdevelopmentPageView.as_view(), name='webdevelopment'),
    path('mobiledevelopment/', MobileDevelopmentPageView.as_view(), name='mobiledevelopment'),
    path('creativedesign/', CreativedesignPageView.as_view(), name='creativedesigns'),
    path('digitalmarketing/',  DigitalmarketingPageView.as_view(), name='digitalmarketing'),
    path('creativedesigns/', ContentwritingPageView.as_view(), name='contentwriting'),
    path('contact/', emailview, name='contact'),
]
