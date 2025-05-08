from rest_framework import serializers
from .models import Gallery, GalleryImage

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']

class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(), write_only=True, required=False
    )

    class Meta:
        model = Gallery
        fields = ['id', 'name', 'images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        gallery = Gallery.objects.create(**validated_data)
        for image in uploaded_images:
            GalleryImage.objects.create(gallery=gallery, image=image)
        return gallery
