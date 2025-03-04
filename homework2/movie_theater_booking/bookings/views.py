from rest_framework import viewsets 
from .models import Movie, Seat, Booking 
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse

# from Django tutorial 
def index(request):
    return HttpResponse("Hello, world. You're at the bookings index.")

# required views (using Django REST Framework's viewsets )
# manages CRUD operations on movies 
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer 

# manages seat availability and booking 
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

# allows users to book seats and view their booking history 
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # create user booking 
    def perform_create(self, serializer):
        booking = serializer.save(user=self.request.user.username)
        booking.seat.booking_status = True # update seat status to booked 
        booking.seat.save()

# HTML pages 
def home(request):
    return render(request, 'bookings/base.html', {})

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request):
    seats = Seat.objects.filter(booking_status=False)
    return render(request, 'bookings/seat_booking.html', {'seats': seats})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def login_view(request):
    return HttpResponse("You have reached the login page.")  # Debug message