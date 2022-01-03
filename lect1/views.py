from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Django. Lecture 1 </h1>')
def hello(request):
    return HttpResponse('<h1>Hello </h1>')
def hello_name(request, name=None):
    return HttpResponse(f'<h1>Hello {name.capitalize()} </h1>')

# Create your views here.