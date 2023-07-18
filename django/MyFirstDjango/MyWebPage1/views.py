from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<center><h2>Hello Wold Python DJANGO!!</h2></center>")