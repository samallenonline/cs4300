# Generated by Django 4.2.11 on 2025-03-04 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_movie_poster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seat',
            old_name='is_booked',
            new_name='booking_status',
        ),
        migrations.AddField(
            model_name='seat',
            name='movie',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='seats', to='bookings.movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seat',
            name='seat_number',
            field=models.CharField(max_length=10),
        ),
    ]
