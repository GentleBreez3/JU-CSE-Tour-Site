from django.shortcuts import render
from basic_app.models import Money
from django.db.models import Sum
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.utils.decorators import method_decorator
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

class MoneyListView(SuperuserRequiredMixin,ListView):

    model = models.Money

    def get_context_data(self, **kwargs):
        context = super(MoneyListView, self).get_context_data(**kwargs)
        context['amount_sum'] = Money.objects.all().aggregate(sum_all=Sum('amount')).get('sum_all')
        return context


class MoneyDetailView(SuperuserRequiredMixin,DetailView):
    context_object_name = 'money_details'
    model = models.Money
    template_name = 'basic_app/money_detail.html'


class MoneyCreateView(SuperuserRequiredMixin,CreateView):
    fields = ("name","roll","amount","batch")
    model = models.Money
    success_url = reverse_lazy("basic_app:list")


class MoneyUpdateView(SuperuserRequiredMixin,UpdateView):
    fields = ("name","roll","amount","batch")
    model = models.Money
    success_url = reverse_lazy("basic_app:list")

class MoneyDeleteView(SuperuserRequiredMixin,DeleteView):
    model = models.Money
    success_url = reverse_lazy("basic_app:list")
