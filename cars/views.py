from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator, Page, EmptyPage
from django.contrib.postgres.search import SearchVector



# Create your views here.
def cars(request):
    
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    # page = paginator.page()
    paged_cars = paginator.get_page(page)
    
    search_fields = {
            'model':[],
            'city':[],
            'year':[],
            'body_style':[]       
            }
    
    for field in search_fields:
        items = Car.objects.values_list(field, flat=True).distinct()
        search_fields[field].extend(items)
        
        data = {
            'cars': paged_cars,
            'search_fields': search_fields
        }

    return render(request, 'cars/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)      
    data = {
            'single_car': single_car,           
        }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars =  Car.objects.order_by('-created_date')
    
     
    search_fields = {
            'model':[],
            'city':[],
            'year':[],
            'body_style':[]       
            }
    
    for field in search_fields:
        items = Car.objects.values_list(field, flat=True).distinct()
        search_fields[field].extend(items)
    # search_fields = [
    #         'model',
    #         'city',
    #         'year',
    #         'type',        
    #     ]
    
    # for field in search_fields:
    #     if field in request.GET:
    #         field = request.GET[field]
    #         if field:            
    #             cars = Car.objects.filter(model__iexact=model)
        
        
        
        
           
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:            
            cars = cars.filter(description__icontains=keyword)
            
    if 'model' in request.GET:
        model = request.GET['model']
        if model:            
            cars = cars.filter(model__iexact=model)
            
    if 'city' in request.GET:
        citykey = request.GET['city']        
        if citykey:
            cars = cars.filter(city__iexact=citykey)
            
    if 'year' in request.GET:
        year = request.GET['year']
        if year:            
            cars = cars.filter(year__iexact=year)
            
    if 'body_style' in request.GET:
        body_style= request.GET['body_style']
        if body_style:            
            cars = cars.filter(body_style__iexact=body_style)
            
    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']
        if max_price:
            cars =  cars.filter(price__gte=min_price, price__lte=max_price)
                                      
        
    data = {
            'cars': cars,
            'search_fields': search_fields
        }
    
    return render(request, 'cars/search.html', data)        
    
