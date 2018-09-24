# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from .models import Car, Fuel, Service, Mileage
from django.urls import reverse


def index(request):
    context = {
    'car_list': Car.objects.order_by('name'),
    'module': 'carcare/index.html',
    'title': 'Garage',
    }
    return render(request, 'carcare/frame.html', context)
    return HttpResponse(template.render(context, request))

def car(request, car_id):
    context = {
        'car': get_object_or_404(Car, pk=car_id),
        'mileage': Mileage.objects.filter(car=car_id).order_by("-date")[:1].get(),
        'mileagelog': Mileage.objects.filter(car=car_id).order_by("-date")[:5],
        'fuel': Fuel.objects.filter(car=car_id).order_by("-date")[:5],
        'module': 'carcare/car.html',
        'title': 'Car Profile',
        'service': Service.objects.filter(car=car_id).order_by("-date")[:5],
        }
    return render(request, 'carcare/frame.html', context)
    return HttpResponse(template.render(context, request))

def service(request, service_id):
    context = {
        'module': 'carcare/service.html',
        'title': 'Car Profile',
        'service': get_object_or_404(Service, pk=service_id),
        }
    return render(request, 'carcare/frame.html', context)
    return HttpResponse(template.render(context, request))

def fuel(request):
    context = {
    'fuel_list': Fuel.objects.order_by('-date'),
    'module': 'carcare/fuel.html',
    'title': 'Fuel Log',
    }
    return render(request, 'carcare/frame.html', context)
    return HttpResponse(template.render(context, request))
