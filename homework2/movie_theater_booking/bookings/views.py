from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# From tutorial 
def index(request):
    return HttpResponse("Hello, world. You're at the bookings index.")

# Required views 
def MovieViewSet(request):
    return HttpResponse("Hello, world. You're at the movie view set.")

def SeatViewSet(request):
    return HttpResponse("Hello, world. You're at the seat view set.")

def BookingViewSet(request):
    return HttpResponse("Hello, world. You're at the booking view set.")