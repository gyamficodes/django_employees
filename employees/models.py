from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250) 

    def __str__(self):
        return f"{self.name} ({self.location})"



class Employee(models.Model):
     first_name = models.CharField(max_length=100)
     last_name = models.CharField(max_length=100)
     email = models.EmailField(unique=True)
     designation = models.CharField(max_length=100)
     salary = models.DecimalField(max_digits=10, decimal_places=2)
     joining_date = models.DateField()
     is_active = models.BooleanField(default=True)
     #  department = models.ForeignKey(Department, on_delete=models.CASCADE)
     department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
     manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

     def __str__(self):
         return f"{self.first_name} {self.last_name}"

     def full_name(self):
         return f"{self.first_name} {self.last_name}"









