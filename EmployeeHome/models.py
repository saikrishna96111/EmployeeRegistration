from django.db import models

# Create Employee with necessary parameters. 
# Create your models here.
class Employeedb(models.Model):
    ssn=models.IntegerField(unique=True,max_length=100,null=True)
    name=models.CharField(max_length=100,null=True)
    email=models.EmailField(max_length=100,null=True)
    password=models.CharField(max_length=100,null=True)
    dob=models.DateField(null=True)
    city=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name