from django.contrib import admin

# Register your models here.

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'status')
    search_fields = ('name', 'designation')
    list_filter = ('status',)

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)