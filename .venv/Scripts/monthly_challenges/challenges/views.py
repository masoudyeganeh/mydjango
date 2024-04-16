from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

def monthly_challenge(request, month):
    x = ""
    if month == "jan":
        x = "jan!"
    elif month == "feb":
        x = "feb!"
    else:
        return HttpResponseNotFound("invalid month")
    return HttpResponse(x)

# Create your views here.
