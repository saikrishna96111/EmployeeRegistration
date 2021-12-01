from django.contrib import admin
from .models import Employeedb
# Register your models here.


@admin.register(Employeedb)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ssn', 'name', 'email','dob', 'city')
    ordering = ('ssn','name')
    search_fields = ('ssn','name', 'email')

# admin.site.register(Employeedb)