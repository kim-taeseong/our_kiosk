from django.urls import path
from . import views

app_name = 'our_kiosk_app'

urlpatterns = [
    path('', views.VarietyListView.as_view(), name='index'),
    path('variety/<int:pk>', views.VarietyDetailView.as_view(), name='detail'),
    path('variety/create/', views.VarietyCreateView.as_view(), name='create_variety'),
    path('variety/<int:pk>/update/', views.VarietyUpdateView.as_view(), name='update_variety'),
    path('variety/<int:pk>/delete/', views.VarietyDeleteView.as_view(), name='delete_variety'),
]