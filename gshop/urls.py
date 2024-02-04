from django.contrib import admin
from django.urls import path, include
from gshop_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('gshop_app.urls')),
    path('student', views.studentApi),
    path('student/<int:student_id>/', views.studentApi),
]
