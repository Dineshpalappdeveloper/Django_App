from django.urls import path
from . import views

urlpatterns = [
    path('list', views.car_list_view, name='car_list'),
    path('book', views.book_list_view, name='book_list'),
    path('product', views.product_list_view, name='product_list'),
    path('product/<int:pk>', views.product_detail_view, name='product_Detail'),
    path('<int:pk>', views.car_detail_view, name='car_detail'),
    path('showroom', views.showroom_View.as_view(), name='car_showroom'),
    path('showroom/<int:pk>', views.showRoomDetails.as_view(),
         name='car_showroom_Data'),
    path('review', views.ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>', views.ReviewDetails.as_view(), name='review_details'),
]
