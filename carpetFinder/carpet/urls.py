from django.urls import path
from . import views


app_name = 'carpet'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),
]