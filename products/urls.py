from django.contrib import admin
from django.urls import path, include  # Import `include`
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Route for the product list
    path('<int:product_id>/', views.product_detail, name='product_detail'),  # Route for the product detail
]