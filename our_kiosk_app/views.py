from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Variety, Beverage

class VarietyListView(ListView):
    model = Variety

class VarietyCreateView(CreateView):
    model = Variety
    fields = ['name']
    success_url = reverse_lazy('our_kiosk_app:index')

class VarietyDetailView(DetailView):
    model = Variety

class VarietyUpdateView(UpdateView):
    model = Variety
    fields = ['name']
    template_name_suffix = '_updates_form'
    success_url = reverse_lazy('our_kiosk_app:index')

class VarietyDeleteView(DeleteView):
    model = Variety
    success_url = reverse_lazy('our_kiosk_app:index')

class BeverageCreateView(CreateView):
    model = Beverage
    fields = ['name', 'variety']
    success_url = reverse_lazy('our_kiosk_app:index')