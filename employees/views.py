from django.shortcuts import render


#Decided which url pattern to create 
#Created a URL pattern for the main urls.py, and forward it to employee.uls  
# Created the view 
#creatted the template for the view


def employee_detail(request, employee_id):
     return render(request, 'employee_detail.html', {'employee_id': employee_id})