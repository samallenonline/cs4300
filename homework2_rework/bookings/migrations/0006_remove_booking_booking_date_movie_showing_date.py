# Generated by Django 4.2.11 on 2025-03-04 10:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_rename_is_booked_seat_booking_status_seat_movie_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='showing_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
