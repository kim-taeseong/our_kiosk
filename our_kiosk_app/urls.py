from django.urls import path
from . import views

urlpatterns = [
    path('', views.VarietyList.as_view(), name='index')
]