from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cabin   

class CabinList(ListView):
    model = Cabin
    template_name = 'cabin/cabin_list.html'
    context_object_name = 'cabins'

class CabinDetail(DetailView):
    model = Cabin
    template_name = 'cabin/cabin_detail.html'
    context_object_name = 'cabin'

class CabinCreate(CreateView):
    model = Cabin
    template_name = 'cabin/cabin_form.html'
    fields = ['name', 'location', 'capacity']
    success_url = reverse_lazy('cabin-list')

class CabinUpdate(UpdateView):
    model = Cabin
    template_name = 'cabin/cabin_form.html'
    fields = ['name', 'location', 'capacity']
    success_url = reverse_lazy('cabin-list')

class CabinDelete(DeleteView):
    model = Cabin
    template_name = 'cabin/cabin_confirm_delete.html'
    context_object_name = 'cabin'
    success_url = reverse_lazy('cabin-list')

    
