from django.contrib import admin

# Register your models here.

from .models import Cabin

# Register your models here.
class CabinAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')
    search_fields = ('name', 'location')
    list_filter = ('location',)


admin.site.register(Cabin)
