from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'myapp/main/index.html')

def categorias(request):
    return render(request, 'myapp/main/categorias.html')