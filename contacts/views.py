from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


# Create your views here.
def inquire(request):
    if request.method=="POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        province = request.POST['province']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
        else:
            has_contacted = Contact.objects.all().filter(car_id=car_id, email=email)
          
        if has_contacted:
            messages.error(request, "You have already submitted an inquiry about this item.")
            return redirect('/cars/'+car_id)
        else:        
            contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need,
                              city=city, province=province, email=email, phone=phone, message=message)
            
            admin_info = User.objects.get(is_superuser=True)
            admin_email = admin_info.email
            
            send_mail('New Car Inquiry' ,
                        'Inquiry about' + car_title + ', please open your admin panel for more information.',
                        'zipyeg222@gmail.com',
                        [admin_email],
                        fail_silently=False,)
                        
                       
            
            contact.save()
        
        messages.success(request, "Your inquiry has been submitted, we will get back to you soon, Thank you.")
        return redirect('/cars/'+car_id)
    
        