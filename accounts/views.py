from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.success(request, 'Username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.success(request, 'Email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                user.save()
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('dashboard')
                # user.save()
                # messages.success(request, 'You are now registered and you can log in')
                # return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')    
    return render(request, 'accounts/register.html')


@login_required(login_url='login')
def dashboard(request):
    user_inquiries = Contact.objects.order_by('-create_date').filter(user_id=request.user.id)
    data = {
        'inquiries': user_inquiries
    }
    return render(request, 'accounts/dashboard.html',data)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
    return redirect('home')