from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<int:carpet_id>/', views.new_conversation, name='new'),
    path('', views.inbox, name='inbox'),
    path('<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
]