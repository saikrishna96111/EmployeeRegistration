from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect,response
from .models import Employeedb
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ListSerializer

import EmployeeHome
import re

#Class added by : Shrivyas, Sai
#
class ListIndividualView(APIView):

    #Function to get the details of one employee using SSN.
    def get_object(self,ssn):
        try:
            return Employeedb.objects.get(ssn=ssn)
        except Employeedb.DoesNotExist:
            raise Http404

    
    def get(self, request, ssn, format=None):
        snippet = self.get_object(ssn)
        serializer = ListSerializer(snippet)
        return Response(serializer.data)

# End of Class: Shrivyas, Sai


class ListView(APIView):

    #Function to get the details of all employees.
    def get(self, request):
        list = Employeedb.objects.all()
        serializer = ListSerializer(list, many=True)
        return Response({"list": serializer.data})
   
   #Function to register an employee.
    def post(self, request):
        employee = request.data.get('employee')
        # Create an article from the above data
        serializer = ListSerializer(data=employee)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' registered successfully".format(employee_saved.name)})

    #Function to update details of an employee.
    def put(self, request, ssn):
        saved_employee = get_object_or_404(Employeedb.objects.all(), ssn=ssn)
        data = request.data.get('employee')
        serializer = ListSerializer(instance=saved_employee, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            employee_saved = serializer.save()
        return Response({"success": "Employee '{}' updated successfully".format(employee_saved.name)})

    #Function to delete an employee.
    def delete(self, request, ssn):
    # Get object with this pk
        saved_employee = get_object_or_404(Employeedb.objects.all(), ssn=ssn)
        name=saved_employee.name
        saved_employee.delete()
        return Response({"message": "Employee with name `{}` has been deleted.".format(name)},status=204)

# End of Function: Shrivyas, Sai


#Function added by : Shrivyas, Sai
#Function To register the employee after the data is entered.
#
def register(request):
    try:
        if(request.method=='POST'):
            ssn=request.POST.get('ssn')
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            cpassword=request.POST.get('cpassword')
            dob=request.POST.get('dob')
            city=request.POST.get('city')
            if(re.match("(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}",password)):
                if(password==cpassword):
                    user = Employeedb.objects.create(ssn=ssn, name=name, email=email, password=password, dob=dob, city=city)
                    user.save()
                    messages.info(request,"User has been registered successfully.")#message will be displayed if the registration is successful.
                else:
                    messages.info(request, "The passwords did not match. Please try again.")
            else:
                messages.info(request, "Password did not match the specified criteria. Please try again.")
    except:
        messages.info(request, 'User with this ssn already exists.')#message will be displayed if another employee has already registered with the same ssn.
        return HttpResponseRedirect('/register')
    return render(request, 'EmployeeHome/register.html')

# End of Function: Shrivyas, Sai

#Function added by : Shrivyas, Sai
#Function To login after registration.
#
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
                print(str(dob))
                city=login_user.city
                context={"ssn":ssn, "name":name,"email":email,"dob":str(dob),"city":city}
                return render(request, 'EmployeeHome/list.html',context)#details will be shown to the employees.
        else:
            return render(request,'EmployeeHome/login.html')
    except:
        print("Invalid credentials")
        messages.info(request,"Please enter valid credentials.")
        return HttpResponseRedirect('/login')

# End of Function: Shrivyas, Sai

#Function added by : Shrivyas, Sai
#Function To show the information.
#
def list(request):
    return render(request, 'EmployeeHome/list.html')

# End of Function: Shrivyas, Sai

#Function added by : Shrivyas, Sai
#Function To handle updation of the current city.
#
def update(request):
    if(request.method=="POST"):
        current_name=request.POST.get('name')
        current_dob=request.POST.get('dob')
        current_city=request.POST.get('current_city')
        if(current_name!=""):
            Employeedb.objects.filter(email=login_email).update(name=current_name)
        if(current_dob!=""):
            Employeedb.objects.filter(email=login_email).update(dob=current_dob)
        if(current_city!=""):
            Employeedb.objects.filter(email=login_email).update(city=current_city)
        # Employeedb.objects.filter(email=login_email).update(city=current_city)
        user2 = Employeedb.objects.get(email=login_email)
        ssn=user2.ssn
        email=user2.email
        name=user2.name
        dob=user2.dob
        city=user2.city
        context={"ssn":ssn, "name":name,"email":email,"dob":str(dob),"city":city}
        messages.info(request,"Your details have been updated.")
        return render(request, 'EmployeeHome/list.html',context)
    return render(request,"EmployeeHome/update.html")

# End of Function: Shrivyas, Sai

#Function added by : Shrivyas, Sai
#Function To Delete account.
#
def delete(request):
    if(request.method=="POST"):
        Employeedb.objects.filter(email=login_email).delete()
        print("Account deleted")
        messages.info(request, 'User account has been deleted successfully.')
        return HttpResponseRedirect('/register')
    return render(request,"EmployeeHome/delete.html")

# End of Function: Shrivyas, Sai