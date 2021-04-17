from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def good_morning_view(request):
    return HttpResponse('<h>good_morning_view</h>')
def good_afternoon_view(request):
    return HttpResponse('<h>good_afternoon_view</h>')
def good_night_view(request):
    return HttpResponse('<h>good_night_view</h>')
