from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images')

    def __str__(self):
        return self.title
    
    class Meta:
        # verbose_name = 'Blog'
        # verbose_name_plural = 'Blogs'
        # ordering = ['-id']
        db_table = 'blogs'
