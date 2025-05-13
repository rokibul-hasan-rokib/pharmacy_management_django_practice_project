from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User

class UserList(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'

class UserDetail(DetailView):
    model = User
    template_name = 'user/user_detail.html'
    context_object_name = 'user'

class UserCreate(CreateView):
    model = User
    template_name = 'user/user_form.html'
    fields = ['name', 'email', 'password', 'phone', 'address']
    success_url = reverse_lazy('user-list')

class UserUpdate(UpdateView):
    model = User
    template_name = 'user/user_form.html'
    fields = ['name', 'email', 'password', 'phone', 'address']
    success_url = reverse_lazy('user-list')

class UserDelete(DeleteView):
    model = User
    template_name = 'user/user_confirm_delete.html'
    context_object_name = 'user'
    success_url = reverse_lazy('user-list')
