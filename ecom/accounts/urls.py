from django.urls import path
from . import  views

#ecom_app urls

urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/',views.register, name = 'register'),
    path('login/', views.log_in, name = 'login'),
    path('otp/', views.otp, name = 'my_otp'),
    path('resend_otp/', views.resend_otp, name = 'resend_otp'),
    path('logout/', views.log_out, name = 'logout'),
    path('reset_pass/', views.reset_password, name = 'reset_pass'),
    
]
