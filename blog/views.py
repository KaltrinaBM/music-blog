from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_blog(request):
    return HttpResponse("Music Blog")
