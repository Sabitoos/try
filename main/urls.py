from django.contrib import admin
from django.urls import path
from django.urls import re_path
from main import views

urlpatterns = [
 path('', views.index),
 re_path(r'^about', views.about),
 re_path(r'^contact', views.contact),
 path('products/', views.products),
 path('products/<int:productid>/', views.products), #по умолчанию
 path('users/', views.users), #по умолчанию
 path('users/<int:id>/<name>/', views.users),
]

