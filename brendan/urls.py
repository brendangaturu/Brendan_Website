from django.urls import path
from .views import HomePageView, ServicesPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('service/', ServicesPageView.as_view(), name='services'),
    
]
