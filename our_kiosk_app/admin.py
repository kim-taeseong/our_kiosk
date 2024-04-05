from django.contrib import admin
from .models import Variety

@admin.register(Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'registration_date')
    search_fields = ('name',)