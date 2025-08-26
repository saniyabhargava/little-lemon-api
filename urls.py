from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, RegisterView
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"menu", MenuItemViewSet, basename="menu")
router.register(r"bookings", BookingViewSet, basename="bookings")

urlpatterns = [
    # Static HTML pages (rubric: serve static HTML with Django)
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("menu-page/", TemplateView.as_view(template_name="menu.html"), name="menu-page"),
    path("book/", TemplateView.as_view(template_name="book.html"), name="book"),

    # API
    path("api/", include(router.urls)),
    path("api/registration/", RegisterView.as_view(), name="registration"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
