from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request):
 return render(request, "main\index.html")

def products(request, productid = 1):
 output = "<h2>Продукт № {0}</h2>".format(productid)
 return HttpResponse(output)

def users(request, id=1, name="Степлер"):
 output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3>".format(id, name)
 return HttpResponse(output)



