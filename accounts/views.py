from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from .models import User

# Create your views here.

def loginview(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            username = User.objects.get(email=email.lower()).username
            user = authenticate(request, username=username, password=password)
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif user.is_staff:
                return redirect('subadmin_index')
            else:
                return redirect('station_index')
        except:
            context = {}
            context['email'] = email
            context['error'] = 'Invalid Credentials'
            return render(request, 'accounts/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('accounts_login')


