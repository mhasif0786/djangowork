from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(request):
    return HttpResponse('<h1>first_view</h1>')
def second_view(request):
    return HttpResponse('<h1>second_view</h1>')
def third_view(request):
    return HttpResponse('<h1>third_view</h1>')
