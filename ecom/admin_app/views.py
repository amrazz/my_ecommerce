from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib import messages,auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# Create your views here
@never_cache
def admin_login(request):
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
        