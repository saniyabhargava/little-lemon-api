from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MenuItem, Booking

User = get_user_model()

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "name", "price", "description", "image"]

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    class Meta:
        model = Booking
        fields = ["id", "user", "name", "guests", "booking_date", "booking_time", "special_requests"]

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ["username", "password", "email"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
