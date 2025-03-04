from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from django.utils.timezone import make_aware
from datetime import datetime, date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# UNIT TESTS
# test that a movie is created successfully
class TestMovieModel(TestCase):
    # create a test movie
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Blade Runner 2049",
            duration=133,
            release_date=date(2017, 10, 6), 
            showing_date=make_aware(datetime(2025, 3, 12, 20, 0))
        )

    # test that the movie was created correctly 
    def test_movie_creation(self):
        movie = Movie.objects.get(title="Blade Runner 2049")
        self.assertEqual(movie.duration, 133)
        self.assertEqual(movie.release_date, date(2017, 10, 6))
        self.assertEqual(movie.showing_date.strftime("%Y-%m-%d %I:%M %p"), "2025-03-12 08:00 PM")

# test that a seat is initially unbooked
class TestSeatModel(TestCase):
    # create a test movie
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Interstellar",
            duration=169,
            release_date=date(2014, 10, 26), 
            showing_date=make_aware(datetime(2025, 3, 7, 21, 30))
        )
        # create a test seat for the movie
        self.seat = Seat.objects.create(seat_number="A1", movie=self.movie, booking_status=False)

    # ensure the seat is unbooked by default (False = Available)
    def test_seat_booking_status(self):
        seat = Seat.objects.get(seat_number="A1")
        self.assertFalse(seat.booking_status)
        self.assertEqual(seat.movie.release_date, date(2014, 10, 26))
        self.assertEqual(seat.movie.showing_date.strftime("%Y-%m-%d %I:%M %p"), "2025-03-07 09:30 PM")

# test that a booking is created successfully 
class TestBookingModel(TestCase):
    # create a test user, movie, and seat
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.movie = Movie.objects.create(
            title="Akira",
            duration=124,
            release_date=date(1989, 12, 25), 
            showing_date=make_aware(datetime(2025, 3, 17, 15, 0))
        )
        self.seat = Seat.objects.create(seat_number="B2", movie=self.movie, booking_status=False)

    # ensure that the booking was created correctly 
    def test_booking_creation(self):
        booking = Booking.objects.create(user=self.user, seat=self.seat, movie=self.movie)
        self.assertEqual(booking.user.username, "test")
        self.assertEqual(booking.seat.seat_number, "B2")
        self.assertEqual(booking.movie.release_date, date(1989, 12, 25)) 
        self.assertEqual(booking.movie.showing_date.strftime("%Y-%m-%d %I:%M %p"), "2025-03-17 03:00 PM")

# INTEGRATION TESTS
class TestAPIEndpoints(TestCase):
    # tests for API endpoints to ensure correct responses 
    def setUp(self):
        # set up test client, user, sample data
        self.client = APIClient()

        # create test user
        self.user = User.objects.create_user(username="apiuser", password="testpass")

        # create test movies
        self.movie1 = Movie.objects.create(
            title="All About Lily Chou Chou",
            duration=157,
            release_date=date(2002, 7, 12),
            showing_date=datetime(2025, 3, 14, 20, 15)
        )
        self.movie2 = Movie.objects.create(
            title="Interstellar",
            duration=169,
            release_date=date(2014, 10, 26),
            showing_date=datetime(2025, 3, 7, 21, 30)
        )

        # create test seats
        self.seat1 = Seat.objects.create(seat_number="A1", movie=self.movie1, booking_status=False)
        self.seat2 = Seat.objects.create(seat_number="B1", movie=self.movie2, booking_status=False)

        # create a test booking
        self.booking = Booking.objects.create(user=self.user, seat=self.seat1, movie=self.movie1)

    # ensure the movie list API returns correect status and data format
    def test_movie_list_api(self):
        url = reverse('movie-list')
        response = self.client.get(url)

        # check if response is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # verify that at least two movies are in the response
        self.assertEqual(len(response.json()), 2)

    # ensure fetching a single movie is successful
    def test_movie_detail_api(self):
        url = reverse('movie-detail', args=[self.movie1.id])
        response = self.client.get(url)

        # check response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check if the returned title matches the expected title
        self.assertEqual(response.json()['title'], "All About Lily Chou Chou")

    # ensure the seat list API returns the correct status and data format
    def test_seat_list_api(self):
        url = reverse('seat-list')
        response = self.client.get(url)

        # check response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # verify there are two seats available
        self.assertEqual(len(response.json()), 2)

    # ensure the booking list API returns the correct data 
    def test_booking_list_api(self):
        url = reverse('booking-list')
        response = self.client.get(url)

        # check response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # verify one booking exists
        self.assertEqual(len(response.json()), 1)

    # ensure a booking can be create via the API
    def test_booking_creation_api(self):
        self.client.force_authenticate(user=self.user)  # authenticate user

        url = reverse('booking-list')  # POST to create a booking
        data = {
            "user": self.user.id,
            "seat": self.seat2.id,
            "movie": self.movie2.id
        }
        response = self.client.post(url, data, format='json')

        # check response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # verify booking exists
        self.assertEqual(Booking.objects.count(), 2)
