from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('<marquee><h1>JAY JAGANNATH SWAMI</h1></marquee>')
