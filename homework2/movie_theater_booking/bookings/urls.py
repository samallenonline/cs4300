from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.movie_list, name='movie_list'),
    path('seats/', views.seat_booking, name='seat_booking'),
    path('history/', views.booking_history, name='booking_history'),
]