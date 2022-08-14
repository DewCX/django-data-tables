from django.shortcuts import render
from App.models import Employee

#Function to render Homepage

def home(request):
    employee_list = Employee.objects.all()
    return render(request, "home.html",{"employees":employee_list})
