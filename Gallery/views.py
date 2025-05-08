from rest_framework import generics
from .models import Gallery
from .serializers import GallerySerializer

class GalleryCreateView(generics.ListCreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
