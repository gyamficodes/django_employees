from django.shortcuts import redirect, render, get_object_or_404
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
    if request.method =='POST':
       form = EmployeeForm(request.POST, request.FILES)
       if form.is_valid():
           form.save()
           return redirect('home')  # Redirect to the employee list view after successful submission
           print_("Form is valid and employee added successfully.")
       else:
           print("Form is not valid:", form.errors)
    form = EmployeeForm()
    context = {
        'form': form
    }
    return render(request, "add_employee.html", context)


def edit_employee(request, employee_id):
      employee = get_object_or_404(Employee, id=employee_id)
      if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=employee.id)  # Redirect to the employee detail view after successful submission
      else:
        form = EmployeeForm(instance=employee)
    
      context = {
        'form': form,
        'employee': employee
    }
      return render(request, "edit_employee.html", context)