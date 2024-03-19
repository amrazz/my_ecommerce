from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.db.models import Q

# Create your views here
@never_cache
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request, 'dashboard.html', {'user' : user})
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        sp_user = authenticate(request, username = username, password = password)
        if sp_user is not None and sp_user.is_superuser:
            auth.login(request, sp_user)
            return redirect('dashboard')
        else:
            messages.error(request,'Sorry, only Admins are allowed.')
            return redirect(admin_login)
        
    return render(request, 'login.html')
def admin_logout(request):
    auth.logout(request)
    return redirect(admin_login)
    

@never_cache
def dashboard(request):
    if request.user.is_superuser:
        
        return render(request, 'dashboard.html')
    else:
        return redirect(admin_login)
def customer(request):
    users = User.objects.all()
    return render(request, 'customer.html',{'users' : users})

def block_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect('customer')

def unblock_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('customer')

def user_search(request):
    if request.method == 'POST':
        get_search = request.POST.get('search')
        
        return_search = User.objects.filter(Q(username__icontains = get_search) | Q(email__icontains = get_search) )
        print(return_search)
        return render(request, 'customer.html', {'users' : return_search})
    else:
        return redirect('customer')
    
        
        
        
        