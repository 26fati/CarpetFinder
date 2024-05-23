from django.urls import path
from . import views


app_name = 'carpet'

urlpatterns = [
    path('add/', views.add, name='add'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('<int:id>/', views.detail, name='detail'),
]