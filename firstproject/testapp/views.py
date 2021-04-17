from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    return HttpResponse('<h1>hello world </h1>')
def myworld(request):
    return HttpResponse('<h1>second one</h1>')
