from django.contrib import admin
from .models import Movie, Seat, Booking

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'poster')  # show poster field in admin

# Register your models here.
admin.site.register(Seat)
admin.site.register(Booking)
admin.site.register(Movie, MovieAdmin)
