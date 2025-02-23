from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    release_date = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    seat_number = models.IntegerField()
    booking_status = models.CharField(max_length=50)

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    booking_date = models.DateField()
