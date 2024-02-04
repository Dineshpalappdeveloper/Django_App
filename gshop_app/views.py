# Correct import statement in views.py
from rest_framework import status
from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse

from gshop_app.api_file.serializers import CarSerializer, StudentSerializer
# Create your views here.
# import django.shortcuts from render
from .models import CarList, Student
from rest_framework.response import Response
# from api_file import CarSerializer
# from .serializers import CarSerializer

from rest_framework.decorators import api_view

# sql connection

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


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


# for mysql connection
@csrf_exempt
def studentApi(request, student_id=0):
    if request.method == 'GET':
        student = Student.objects.all()
        student_serializer = StudentSerializer(student, many=True)
        return JsonResponse(student_serializer.data, safe=False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Student.objects.get(id=student_id)
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        student = Student.objects.get(id=student_id)
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)
