
from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def timing(request):
    time=datetime.datetime.now()
    s=str(time) 
    return HttpResponse(s)
