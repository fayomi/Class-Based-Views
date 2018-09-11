from django.shortcuts import render
from django.views.generic import View, TemplateView,ListView,DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'cbv/index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'cbv/school_detail.html'
