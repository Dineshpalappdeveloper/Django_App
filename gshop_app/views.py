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


def car_detail_view(requst, pk):
    car = CarList.objects.get(pk=pk)
    data = {
        "name": car.name,
        "description": car.description,
        "active": car.active,
    }
    return JsonResponse(data)
