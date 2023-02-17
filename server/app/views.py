from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from . import models

# Create your views here.
def index(request):
    return HttpResponse("Hello, World! Main Page Speaking!")

def carlist(request):
    cars = models.Car.objects.all()
    car_count = cars.count()
    context = {
        'count': car_count,
        'car_list': cars
    }

    return render(request, 'showroom/car_list.html', context)

def carDetail(request, car_id):
    car_detail = get_object_or_404(models.Car, id=car_id)
    #if car_detail is None:
        #raise Http404(f"Car of id {car_id} does not exist or you do not have access to it.")

    template = loader.get_template('showroom/car_detail.html')
    context = {
        'car_id': car_id,
        'car_detail': car_detail
    }
    return HttpResponse(template.render(context, request))