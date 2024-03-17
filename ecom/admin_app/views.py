from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

# Create your views here.
@login_required
def log_in(request):
    if request.user.is_superuser:
        user = User.objects.all()
        context = {'user' : user}
        return render(request, 'dashboard.html', context)
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        sp_user = auth.authenticate(request, email = email, password = password)
        if sp_user is not None and sp_user.is_superuser:
            login(request, sp_user)
            return redirect('dashboard')
        else:
            messages.error(request,'Sorry, only Admins are allowed.')
            return redirect('log_in')

    return render(request, 'login.html')
def log_out(request):
    logout(request)
    return redirect(log_in)
    

@never_cache
def dashboard(request):
    return render(request, 'dashboard.html')