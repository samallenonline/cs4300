from django.shortcuts import render
from rest_framework import viewsets 
from .models import Movie, Seat, Booking 
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer 
from rest_framework.permissions import IsAuthenticated 

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

    # only return available seats (booking status is false)
    def get_queryset(self):
        return Seat.objects.filter(booking_status=False)

# allows users to book seats and view their booking history 
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    # return user's personal booking history
    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user.username)

    # create user booking 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.username)
        booking.seat.booking_status = True # update seat status to booked 
        booking.seat.save()