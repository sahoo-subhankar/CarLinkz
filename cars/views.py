from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city',flat=True).distinct()
    year_fields = Car.objects.values_list('year',flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style',flat=True).distinct()
    data = {
        'cars': paged_cars,
        'model_fields': model_fields,
        'city_fields': city_fields,
        'year_fields': year_fields,
        'body_style_fields': body_style_fields,
    }
    return render(request, 'cars/cars.html',data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html',data)

def search(request):
    cars = Car.objects.order_by('-created_date')
    
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city',flat=True).distinct()
    year_fields = Car.objects.values_list('year',flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style',flat=True).distinct()
    transmission_fields = Car.objects.values_list('transmission',flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if 'keyword':
            cars = cars.filter(description__icontains=keyword)
        else:
            pass
        
    if 'model' in request.GET:
        model = request.GET['model']
        if 'model':
            cars = cars.filter(model__iexact=model)
        else:
            pass
        
    if 'city' in request.GET:
        city = request.GET['city']
        if 'city':
            cars = cars.filter(city__iexact=city)
        else:
            pass
        
    if 'year' in request.GET:
        year = request.GET['year']
        if 'year':
            cars = cars.filter(year__iexact=year)
        else:
            pass
    
    if 'body_type' in request.GET:
        body_type = request.GET['body_type']
        if 'body_type':
            cars = cars.filter(body_type__iexact=body_type)
        else:
            pass
        
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if 'max_price':
            cars = cars.filter(price__gte=min_price, price__lte=max_price)
        else:
            pass

    data = {
        'cars': cars,
        'model_fields': model_fields,
        'city_fields': city_fields,
        'year_fields': year_fields,
        'body_style_fields': body_style_fields,
        'transmission_fields': transmission_fields,
    }
    return render(request, 'cars/search.html',data)