from django.contrib import admin
from .models import Employee, Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [ 'full_name', 'email', 'designation', 'salary', 'joining_date', 'is_active', 'department', 'manager']
    list_filter = ('is_active', 'department')
    search_fields = ('full_name', 'email', 'designation')
    list_editable = ['is_active', 'department', 'manager']



# Register your models here.
admin.site.register(Department)
admin.site.register(Employee, EmployeeAdmin)