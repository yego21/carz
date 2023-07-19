from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Team
from cars.models import Car

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
    return render(request, 'pages/contact.html')
        
