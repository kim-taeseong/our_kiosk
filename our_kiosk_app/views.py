from django.views.generic import ListView
from .models import Variety, Beverage

class VarietyList(ListView):
    model = Variety