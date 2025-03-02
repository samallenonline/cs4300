from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('movies/', views.movie_list, name='movie_list'),  # movie list HTML page
    path('seats/', views.seat_booking, name='seat_booking'),    # seat booking HTML page
    path('history/', views.booking_history, name='booking_history'),  # booking history HTML page
]
