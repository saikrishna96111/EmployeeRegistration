from django.shortcuts import render,redirect
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

def login(request):
    global login_email
    if(request.method=='POST'):
        email=request.POST.get('email')
        password=request.POST.get('password')
        login_user=Employeedb.objects.get(email=email, password=password)
        if(login_user):
            ssn=login_user.ssn
            email=login_user.email
            login_email=email
            name=login_user.name
            dob=login_user.dob
            city=login_user.city
            context={"ssn":ssn, "name":name,"email":email,"dob":dob,"city":city}
            return render(request, 'EmployeeHome/update.html',context)
    else:
        return render(request,'EmployeeHome/login.html')

def update(request):
    return render(request, 'EmployeeHome/update.html')

def update2(request):
    if(request.method=="POST"):
        current_city=request.POST.get('current_city')
        Employeedb.objects.filter(email=login_email).update(city=current_city)
        user2 = Employeedb.objects.get(email=login_email)
        ssn=user2.ssn
        email=user2.email
        name=user2.name
        dob=user2.dob
        city=user2.city
        context={"ssn":ssn, "name":name,"email":email,"dob":dob,"city":city}
        return render(request, 'EmployeeHome/update.html',context)
    return render(request,"EmployeeHome/update2.html")

def delete(request):
    if(request.method=="POST"):
        Employeedb.objects.filter(email=login_email).delete()
        print("Account Deleted")
        return redirect('/register')
    return render(request,"EmployeeHome/delete.html")