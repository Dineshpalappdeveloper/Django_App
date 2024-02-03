# Correct import statement in views.py
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
# import django.shortcuts from render
from .models import CarList


def car_list_view(requst):
    cars = CarList.objects.all()
    data = {
        "cars": list(cars.values()),
    }

    return JsonResponse(data)


def car_detail_view(request, pk):
    car = CarList.objects.get(id=pk)
    data = {
        "name": car.name,
        "description": car.description,
        "active": car.is_active,
    }
    return JsonResponse(data)
