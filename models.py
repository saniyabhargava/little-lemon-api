from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)  # keep it simple (URL)
    def __str__(self):
        return f"{self.name} - {self.price}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=120)            # person making booking
    guests = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("booking_date", "booking_time", "name")  # simple safety

    def __str__(self):
        return f"{self.name} @ {self.booking_date} {self.booking_time} ({self.guests})"
