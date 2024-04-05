from django.urls import path
from . import views

app_name = 'our_kiosk_app'

urlpatterns = [
    path('', views.VarietyListView.as_view(), name='index')
]