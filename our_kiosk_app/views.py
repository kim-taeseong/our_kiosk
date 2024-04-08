from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
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