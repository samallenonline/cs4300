from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Utilize templates 

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})


def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)  # Get the selected movie
    seats = Seat.objects.filter(movie=movie, booking_status=False)  # Show only available seats for this movie

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id, movie=movie)  # Ensure the seat belongs to this movie
        seat.booking_status = True  # Mark the seat as booked
        seat.save()

        Booking.objects.create(user=request.user, seat=seat, movie=movie)  # Save booking with correct movie
        return redirect('booking_history')

    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})