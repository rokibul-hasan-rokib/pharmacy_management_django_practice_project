from django.contrib import admin

# Register your models here.

from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email')
    list_filter = ('phone',)

    def has_delete_permission(self, request, obj=None):
        return False
