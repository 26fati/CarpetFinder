from django.urls import path
from . import views


app_name = 'carpet'

urlpatterns = [
    path('add/', views.add, name='add'),
]