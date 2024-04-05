from django.views.generic import ListView, CreateView
from .models import Variety, Beverage

class VarietyListView(ListView):
    model = Variety