from django.shortcuts import render
from django.http import HttpResponseRedirect,response
from .models import Employeedb
import EmployeeHome
# Create your views here.
def register(request):
    if(request.method=='POST'):
        ssn=request.POST.get('ssn')
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        dob=request.POST.get('dob')
        city=request.POST.get('city')
        user = Employeedb.objects.create(ssn=ssn, name=name, email=email, password=password, dob=dob, city=city)
        user.save()
        print("ssn-{}".format(ssn))
    return render(request, 'EmployeeHome/register.html')