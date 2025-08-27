from django.db import models
from django.contrib.auth.models import User


class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ('BUS', 'Bus'),
        ('TRAIN', 'Train'),
        ('FLIGHT', 'Flight'),
        ('CAB', 'Cab'),
    ]
    type = models.CharField(max_length=10, choices=TRAVEL_TYPES, default="BUS")
    source = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()   
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.get_type_display()} from {self.source} to {self.destination}"


class Booking(models.Model):
    BOOKING_STATUS = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(
        User, related_name="bookings", on_delete=models.SET_NULL, null=True, blank=True
    )
    travel_option = models.ForeignKey(
        TravelOption, related_name="bookings", on_delete=models.CASCADE
    )
    number_of_seats = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=BOOKING_STATUS, default='PENDING'
    )

    def __str__(self):
        return f"Booking {self.id} - {self.customer} - {self.status}"

