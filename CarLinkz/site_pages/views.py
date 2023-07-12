from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city',flat=True).distinct()
    year_fields = Car.objects.values_list('year',flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_fields': model_fields,
        'city_fields': city_fields,
        'year_fields': year_fields,
        'body_style_fields': body_style_fields,
    }
    return render(request, 'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html',data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']
        
        email_subject = "New Contact Inquiry from CarZone: " + subject
        message_body = 'Name: ' + name + ". Phone: " + phone + ". Email: " + email + ". Sent the following message:\n\n" + message
        
        email_from = settings.EMAIL_HOST_USER
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            email_subject,
            message_body,
            email_from,
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, 'Thank you for contacting us, a realtor will get back to you soon')
        return redirect('contact')
    return render(request, 'pages/contact.html')
