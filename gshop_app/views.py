# Correct import statement in views.py
from rest_framework import status
from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from gshop_app.api_file.serializers import CarSerializer, StudentSerializer, BookSerializer, ProductSerializer, ShowRoomsListSerializer, ReviewSerializer
# Create your views here.
# import django.shortcuts from render
from .models import CarList, Student, Book, Product, ShowRoomsList, Review
from rest_framework.response import Response
# from api_file import CarSerializer
# from .serializers import CarSerializer

from rest_framework.decorators import api_view

# sql connection
from rest_framework import mixins
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class showroom_View(APIView):
    # authentication_classes = [BaseAuthentication]
    # permission_classes = [IsAuthenticated] // only authenticated persion have access
    # permission_classes = [AllowAny] // anyone can access
    # permission_classes = [IsAdminUser] // only admin have access

    #    session authentication
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated] // only authenticated persion have access
    # permission_classes = [AllowAny] // anyone can access
    # permission_classes = [IsAdminUser] // only admin have access

    def get(self, request):
        showrooms = ShowRoomsList.objects.all()

        serializer = ShowRoomsListSerializer(
            showrooms, many=True, context={'request': request})
        return Response(serializer.data,)

    def post(self, request):
        serializer = ShowRoomsListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Return a 201 Created response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return a 400 Bad Request response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class showRoomDetails(APIView):
    def get(self, request, pk):
        try:
            showroom = ShowRoomsList.objects.get(id=pk)
        except ShowRoomsList.DoesNotExist:
            return Response({'error': 'showroom not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowRoomsListSerializer(showroom,)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            showroom = ShowRoomsList.objects.get(id=pk)
            serializer = ShowRoomsListSerializer(showroom, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Log the exception and print the request data
            print(f"Exception: {e}")
            print(f"Request data: {request.data}")
            return Response({"detail": "Error processing the request"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        showroom = ShowRoomsList.objects.get(id=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


# about book

@api_view(['GET', 'POST'])
def book_list_view(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Return a 201 Created response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        # Fetch products
        products = Product.objects.filter(id=4)

        # Serialize the data
        # Assuming multiple products can be returned
        serializer = ProductSerializer(products, many=True)

        # Return the response with serialized data
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Return a 201 Created response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
