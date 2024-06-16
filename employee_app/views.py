from django.shortcuts import render
from django.http import HttpResponseRedirect
from employee_app.models import  employee_models
from  employee_app.forms import  employee_forms


# Create your views here.

def index(request):
    return render(request,'employee_app/home.html')

def create_view(request):
    form=employee_forms()
    if request.method=="POST":
        form=employee_forms(request.POST)
        form.save()
        return  HttpResponseRedirect('../display')
    return render(request,'employee_app/insert.html',{"form":form})

def retrieve_view(request):
    employee=employee_models.objects.all()
    return render(request, 'employee_app/index.html', {"employee": employee})

def update_view(request,uid):
    employee=employee_models.objects.get(id=uid)
    if request.method=='POST':
        form=employee_forms(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../display')
    else:
        form=employee_forms(instance=employee)
    return render(request,'employee_app/update.html',context={"form":form})

def delete_view(request,did):
    employee=employee_models.objects.get(id=did)
    employee.delete()
    return HttpResponseRedirect('../display')


