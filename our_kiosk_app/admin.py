from django.contrib import admin
from .models import Variety, Beverage

@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'registration_date')
    search_fields = ('name',)

@admin.register(Beverage)
class Beverage(admin.ModelAdmin):
    list_display = ('id', 'name', 'registration_date', 'variety')
    search_fields = ('name',)