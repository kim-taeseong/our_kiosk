from django.urls import path
from . import views

urlpatterns = [
    path('', views.VarietyListView.as_view(), name='index')
]