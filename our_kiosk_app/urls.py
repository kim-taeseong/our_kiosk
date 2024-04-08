from django.urls import path
from . import views

app_name = 'our_kiosk_app'

urlpatterns = [
    path('', views.VarietyListView.as_view(), name='index'),
    path('variety/create/', views.VarietyCreateView.as_view(), name='create_variety'),
]