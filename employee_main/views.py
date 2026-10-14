# from django.http import HttpResponse
from employees.models import Employee  #employee models import Employee
from django.shortcuts import render #render function to render the template (html) and pass the data to the template


def home(request):
        # Fetch the data from the Employee model and pass it to the template
          # return HttpResponse(employees) 
        employees = Employee.objects.all()
        context = {
            'employees': employees
        }
        return render(request, 'home.html', context)









