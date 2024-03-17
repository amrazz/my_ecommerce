from django.urls import path
from . import  views


# Admin_app urls

urlpatterns = [
    path('login/', views.log_in, name = 'admin'),
    path('logout/', views.log_out, name = 'logout'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    
]
