from django.urls import path
from . import  views


# Admin_app urls

urlpatterns = [
    path('admin_login/', views.admin_login, name = 'admin_login'),
    path('admin_logout/', views.admin_logout, name = 'admin_logout'),
    path('dashboard/', views.dashboard, name ='dashboard'),
    path('customer/', views.customer, name = 'customer'),
    path('block-user/<int:user_id>/', views.block_user, name='block_user'),
    path('unblock-user/<int:user_id>/', views.unblock_user, name='unblock_user'),
    path('user_search/', views.user_search, name = 'user_search'),
    
    
]
