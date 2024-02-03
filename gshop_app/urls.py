from django.urls import path
from . import views

urlpatterns = [
    path('list', views.car_list_view, name='car_list'),
]
