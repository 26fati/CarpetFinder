from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views



app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views._logout, name='logout'),
    path('search/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
]