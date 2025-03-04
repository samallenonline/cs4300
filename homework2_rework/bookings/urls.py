from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet
from . import views
from django.contrib.auth.views import LoginView, LogoutView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API endpoints
    path('', views.movie_list, name='movie_list'),  # Default page (Movie list)
    path('movies/', views.movie_list, name='movie_list'),
    path('seats/', views.seat_booking, name='seat_booking'),
    path('history/', views.booking_history, name='booking_history'),
]
