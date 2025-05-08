from django.urls import path
from .views import GalleryCreateView

urlpatterns = [
    path('galleries/', GalleryCreateView.as_view(), name='gallery-create'),
]
