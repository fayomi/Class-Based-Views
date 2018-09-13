from django.shortcuts import render
from django.views.generic import (View,
TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from . import models
from django.urls import reverse_lazy



class IndexView(TemplateView):
    template_name = 'cbv/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv/school_detail.html'


class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('cbv:list')
