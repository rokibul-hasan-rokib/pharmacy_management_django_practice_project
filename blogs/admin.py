from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('title',)
    # prepopulated_fields = {'slug': ('title',)}

admin.site.site_header = "Blog Admin"
admin.site.site_title = "Blog Admin Portal"