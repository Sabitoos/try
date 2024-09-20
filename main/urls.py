from django.contrib import admin
from django.urls import path
from django.urls import re_path
from main import views
from django.views.generic import TemplateView

urlpatterns = [
 path('', views.index),
 path('about/', TemplateView.as_view(template_name="main/about.html")),
 path('contact/', TemplateView.as_view(template_name="main/contact.html",
                                       extra_context={"work": "Разработка програмных продуктов"})),
 path('products/', views.products),
 path('products/<int:productid>/', views.products), #по умолчанию
 path('users/', views.users), #по умолчанию
 path('users/<int:id>/<name>/', views.users),
]

