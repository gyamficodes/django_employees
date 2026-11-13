from django import forms
from employees.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ['name', 'position', 'department', 'salary'] this is ude if you want custom fileds
        fields = '__all__' # This will include all fields from the Employee model
        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
        }