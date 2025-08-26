from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, RegisterSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("name")
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]  # menu is public (GET). POST by admin via admin panel.

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]

    def get_queryset(self):
        # each user sees only their bookings; staff sees all
        if self.request.user.is_staff:
            return Booking.objects.all().order_by("-booking_date", "-booking_time")
        return Booking.objects.filter(user=self.request.user).order_by("-booking_date", "-booking_time")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
