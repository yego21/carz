from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    teams = Team.objects.all()
    search_fields = {
            'model':[],
            'city':[],
            'year':[],
            'body_style':[]       
            }
    for field in search_fields:
        items = Car.objects.values_list(field, flat=True).distinct()
        search_fields[field].extend(items)
    
    featured_cars = Car.objects.order_by('created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('created_date')
    data = {
            'teams': teams,  
            'featured_cars': featured_cars,
            'all_cars': all_cars,
            'search_fields': search_fields
    }
    return render(request, 'pages/home.html', data)
    

def about(request):
    teams = Team.objects.all()
    data = {
            'teams': teams, 
            }
    return render(request, 'pages/about.html', data)

def cars(request):   
    return render(request, 'pages/cars.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    
    if request.method=="POST":
        full_name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
       
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        message_body = "From: " + full_name +"\nEmail address: " +email+ "\nContact No.: "+ phone + "\n\n" + message    
    
        send_mail(subject,
                    message_body,
                    'zipyeg222@gmail.com',
                    [admin_email],
                    fail_silently=False,)
        
        messages.success(request, "Thank you for contacting us, we will reach out to you soon.")
        return redirect('contact')
    
    return render(request, 'pages/contact.html')
        
