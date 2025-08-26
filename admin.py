from django.contrib import admin
from .models import MenuItem, Booking

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "guests", "booking_date", "booking_time", "user")
    list_filter = ("booking_date",)
