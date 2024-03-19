from django.urls import path
from . import  views


# Admin_app urls

urlpatterns = [
    path('admin_login/', views.admin_login, name = 'admin_login'),
    path('admin_logout/', views.admin_logout, name = 'admin_logout'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    
]
