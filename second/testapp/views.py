from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show_curr_time(request):
    return HttpResponse('<h>hello second project</h>')
