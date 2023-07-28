from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as signin, logout as signout
from contacts.models import Contact
from django.contrib.auth.decorators import login_required



# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST["username"]
        password=request.POST["password"]
        
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            signin(request, user)
            return redirect("dashboard")
            messages.success(request, "You are now logged in.")
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect("login")
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists.")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists.")
                return redirect('signup')
            else:
                new_user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password, email=email)
                new_user.save() 
                messages.success(request, "You are registered successfully.")
                return redirect('login')
                
        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
    else:        
        return render(request, 'accounts/signup.html')

@login_required(login_url='login')
def dashboard(request):    
    user_id = request.user.id
    user_inquiry = Contact.objects.order_by('create_date').filter(user_id=user_id)
    data = {
           'inquiries': user_inquiry
        }
    return render(request, 'accounts/dashboard.html', data)

def logout(request):
    if request.method == "POST":
        signout(request)
        messages.success(request, "Successfully logged out.")
        return redirect('home') 
    return redirect('home')

    
   
    
