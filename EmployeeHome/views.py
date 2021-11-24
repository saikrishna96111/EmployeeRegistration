from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,response
from .models import Employeedb
from django.contrib import messages
import EmployeeHome
import js2py

# Create your views here.
# To register the employee after the data is entered.
def register(request):
    try:
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
            messages.info(request,'Registered Successfully')#message will be displayed if the registration is successful.
    except:
        print("SSN is already registered.")
        messages.info(request, 'SSN is already registered!!')#message will be displayed if another employee has already registered with the same ssn.
        return HttpResponseRedirect('/register')
    return render(request, 'EmployeeHome/register.html')

#To login after registration
def login(request):
    global login_email  #Accessing the same email after employee logs in for other operations.
    try:
        if(request.method=='POST'):
            email=request.POST.get('email')
            password=request.POST.get('password')
            login_user=Employeedb.objects.get(email=email, password=password)#checks the data entered with the data in database.
            if(login_user):
                ssn=login_user.ssn
                email=login_user.email
                login_email=email
                name=login_user.name
                dob=login_user.dob
                city=login_user.city
                context={"ssn":ssn, "name":name,"email":email,"dob":dob,"city":city}
                return render(request, 'EmployeeHome/update.html',context)#details will be shown to the employees.
        else:
            return render(request,'EmployeeHome/login.html')
    except:
        print("Invalid Credentials")
        messages.info(request,"Invalid Credentials")
        return HttpResponseRedirect('/login')
#just show the information        
def update(request):
    return render(request, 'EmployeeHome/update.html')

#handles updation of the current city.
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

#Delete account
def delete(request):
    if(request.method=="POST"):
        Employeedb.objects.filter(email=login_email).delete()
        print("Account Deleted")
        messages.info(request, 'Account Deleted')
        return HttpResponseRedirect('/register')
        #return redirect('/register')
    return render(request,"EmployeeHome/delete.html")