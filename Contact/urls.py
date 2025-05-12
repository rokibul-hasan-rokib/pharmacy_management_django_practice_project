from django.urls import path
from .views import ContactView, ThankYouView

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('thank-you/', ThankYouView.as_view(), name='thank_you'),
]