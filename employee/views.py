from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Employee

class EmployeeList(ListView):
    model = Employee
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'
    context_object_name = 'employee'

class EmployeeCreate(CreateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['name', 'designation', 'status']
    success_url = reverse_lazy('employee-list')

class EmployeeUpdate(UpdateView):
    model = Employee
    template_name = 'employee/employee_form.html'
    fields = ['name', 'designation', 'status']
    success_url = reverse_lazy('employee-list')

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'employee/employee_confirm_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-list')