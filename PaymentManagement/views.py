from django.shortcuts import render,HttpResponse
from django.http import request


def home(request):
    return render(request,"home.html")