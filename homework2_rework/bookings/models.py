from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes 
    release_date = models.DateField()
    showing_date = models.DateTimeField()  
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)  

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")  # link seats to movies
    seat_number = models.CharField(max_length=10)
    booking_status = models.BooleanField(default=False)  # False = Available, True = Booked

    def __str__(self):
        return f"{self.movie.title} - Seat {self.seat_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.seat.seat_number})"
