# Correct import statement in views.py
from rest_framework import status
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
def car_list_view(request):
    if request.method == 'GET':
        cars = CarList.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Return a 201 Created response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return a 400 Bad Request response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def car_detail_view(request, pk):
    try:
        car = CarList.objects.get(id=pk)
    except CarList.DoesNotExist:
        return Response({'error': 'car not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarSerializer(car)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
