from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models

class SuperuserRequiredMixin(object):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(SuperuserRequiredMixin, self).dispatch(*args, **kwargs)

class IndexView(SuperuserRequiredMixin,TemplateView):

    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class StudentsListView(ListView):

    model = models.Students

class StudentsDetailView(SuperuserRequiredMixin,DetailView):
    context_object_name = 'students_details'
    model = models.Students
    template_name = 'tour/students_detail.html'


class StudentsCreateView(CreateView):
    fields = ("name","roll","batch")
    model = models.Students
    success_url = reverse_lazy("tour:list")


class StudentsUpdateView(SuperuserRequiredMixin,UpdateView):
    fields = ("name","roll","batch")
    model = models.Students
    success_url = reverse_lazy("tour:list")

class StudentsDeleteView(SuperuserRequiredMixin,DeleteView):
    model = models.Students
    success_url = reverse_lazy("tour:list")
