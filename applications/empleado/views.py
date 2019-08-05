from django.shortcuts import render, redirect  
from applications.empleado.forms import EmployeeForm  
from applications.empleado.models import Employee  

# Create your views here.
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/empleado/list')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'empleado/create.html',{'form':form}) 

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"empleado/list.html",{'employees':employees}) 

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'empleado/edit.html', {'employee':employee})

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/empleado/list")
    return render(request, 'empleado/edit.html', {'employee': employee})

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/empleado/list")