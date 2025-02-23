from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("", views.MovieViewSet, name="MovieViewSet"),
    path("", views.SeatViewSet, name="SeatViewSet"),
    path("", views.BookingViewSet, name="BookingViewSet")
]