from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello world, this is polls index and a sample commit. hello travis?")
