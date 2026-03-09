from django.shortcuts import render, redirect
from .forms import RegisterForm 
from .models import Register   
from django.contrib import messages


# Create your views here.
def landing(request):
    return render(request, 'landingPage.html')

def index(request):
    return render(request, 'index.html')  

def dashboard(request):
    return render(request, 'dashboard.html')

def incidents(request):
    return render(request, 'incidents.html')

def live_monitor(request):
    return render(request, 'live_monitor.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Register.objects.filter(username=username, password=password)
        if user:
            messages.success(request, 'Login successful')   
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():             
            form.save()
            print("Registration successful")    
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})  

def accounts(request):
    return render(request, 'accounts.html') 

def settings(request):
    return render(request, 'settings.html')

def camera(request):
    return render(request, 'camera.html')

def reports(request):
    return render(request, 'reports.html')

def heatmap(request):
    return render(request, 'heatmap.html')

def notification(request):
    return render(request, 'notification.html')
    
def floor_map(request):
    return render(request, 'floor_maps.html')

def privacy_logs(request):
    return render(request, 'privacy_logs.html')

def system_config(request):
    return render(request, 'system_config.html')

def staff_portal(request):
    return render(request, 'staff_portal.html')

def history(request):
    return render(request, 'history.html')




    
