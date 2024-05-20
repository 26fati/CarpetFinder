from django.urls import path
from . import views
from .forms import LoginForm


app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
]