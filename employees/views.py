from django.shortcuts import render, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

#Decided which url pattern to create 
#Created a URL pattern for the main urls.py, and forward it to employee.uls  
# Created the view 
#creatted the template for the view


# employee detail  
def employee_detail(request, employee_id):
     # Fetch the employee object based on the provided employee_id
     employee = get_object_or_404(Employee, id=employee_id)
     context = {
     'employee': employee
     }
     return render(request, 'employee_detail.html', context)


# add employee 
def add_employee(request):
    form = EmployeeForm()
    context = {
        'form': form
    }
    return render(request, "add_employee.html", context)