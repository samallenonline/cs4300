from django.contrib import admin
from .models import Movie, Seat, Booking

class MovieAdmin(admin.ModelAdmin):
    # fields to show in admin
    list_display = ('title', 'release_date', 'duration', 'poster', 'showing_date')

# Register your models here.
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(Movie, MovieAdmin)
