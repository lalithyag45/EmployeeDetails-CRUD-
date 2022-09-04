from .forms import Employeeform, Deleteform, Updateform
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from.models import Employee


def index(request):
    return render(request, 'emp/index.html')
# Create your views here.


def input(request):
    form = Employeeform()
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            Empnum = form.cleaned_data['Empnum']
            Empname = form.cleaned_data['Empname']
            salary = form.cleaned_data['salary']
            address = form.cleaned_data['address']
            e = Employee(Empnum=Empnum, Empname=Empname,
                         salary=salary, address=address)
            e.save()
            return HttpResponseRedirect('../display')
    return render(request, 'emp/input.html', {'form': form})


def display(request):
    lst = Employee.objects.all()
    return render(request, 'emp/display.html', {'lst': lst})


def delete(request):
    form = Deleteform()
    if request.method == 'POST':
        form = Deleteform(request.POST)
        if form.is_valid():
            Empnum = form.cleaned_data['Empnum']
            e = Employee.objects.get(Empnum=Empnum)
            e.delete()
            return HttpResponseRedirect('../display')
    return render(request, 'emp/delete.html', {'form': form})


def update(request):
    form = Updateform()
    if request.method == 'POST':
        form = Updateform(request.POST)
        if form.is_valid():
            Empnum = form.cleaned_data['Empnum']
            Empname = form.cleaned_data['Empname']
            e = Employee.objects.get(Empnum=Empnum)
            e.Empname = Empname
            e.save()
            return HttpResponseRedirect('../display')
    return render(request, 'emp/update.html', {'form': form})
