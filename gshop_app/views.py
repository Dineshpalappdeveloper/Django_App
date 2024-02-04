# Correct import statement in views.py
from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse

from gshop_app.api_file.serializers import CarSerializer
# Create your views here.
# import django.shortcuts from render
from .models import CarList
from rest_framework.response import Response
# from api_file import CarSerializer
# from .serializers import CarSerializer

from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def car_list_view(requst):
    if requst.method == 'GET':
        car = CarList.objects.all()
        serializer = CarSerializer(car, many=True)
        return Response(serializer.data)
    if requst.method == 'POST':
        serializer = CarSerializer(data=requst.data)
        if serializer.is_valid():
            serializer.save()
        else:

            return Response(serializer.errors)


@api_view(['GET', 'PUT'])
def car_detail_view(requst, pk):
    if requst.method == 'GET':
        car = CarList.objects.get(id=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    if requst.method == 'PUT':
        car = CarList.objects.get(id=pk)
        serializer = CarSerializer(car, data=requst.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

# def car_list_view(requst):
#     cars = CarList.objects.all()
#     data = {
#         "cars": list(cars.values()),
#     }

#     return JsonResponse(data)


# def car_detail_view(request, pk):
#     car = CarList.objects.get(id=pk)
#     data = {
#         "name": car.name,
#         "description": car.description,
#         "active": car.is_active,
#     }
#     return JsonResponse(data)

# we can send data with use JsonResponse ?
# Yes use https


# def car_list_view(requst):
#     cars = CarList.objects.all()
#     data = {
#         "cars": list(cars.values()),
#     }
#     data_json = json.dumps(data)
#     return HttpResponse(data_json, content_type="application/json")
