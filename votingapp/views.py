from django.shortcuts import render
from . models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'general/index.html')

def user_register(request):
    return render(request, 'user/user_register.html')

def user_registration(request):
    if request.method == 'POST':

        name = request.POST['name']
        mob = request.POST['mobile_number']
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return render(request, 'user/user_register.html')

        if User.objects.filter(mobile_number=mob).exists():
            messages.error(request, 'Mobile number is already registered.')
            return render(request, 'user/user_register.html')
                
        user = User.objects.create_user(
            name=name,
            mobile_number=mob,
            username=username,
            password=password,
            is_user=True,
        )
                
        return redirect('index') 
    
    return render(request, 'user/user_register.html')



def user_login(request):
    if request.method == 'POST':
        username_or_number = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username_or_number).first()
        
        if user is not None and user.check_password(password) and user.is_user:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'user/user_login.html')


def user_home(request):
    return render(request, 'user/user_home.html')