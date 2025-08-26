from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import MenuItem, Booking
from datetime import date, time

class APISmokeTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="alice-pass", email="a@example.com")
        MenuItem.objects.create(name="Pasta", price="12.50", description="Classic", image="")
        MenuItem.objects.create(name="Salad", price="8.00", description="Green", image="")

    def auth(self):
        url = reverse("token_obtain_pair")
        res = self.client.post(url, {"username":"alice","password":"alice-pass"}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        return res.data["access"]

    def test_menu_list_public(self):
        res = self.client.get("/api/menu/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(res.data), 2)

    def test_booking_crud_requires_auth(self):
        # unauthenticated create should fail
        res = self.client.post("/api/bookings/", {
            "name":"Alice", "guests":2, "booking_date":"2030-01-01", "booking_time":"19:00", "special_requests":""
        }, format="json")
        self.assertIn(res.status_code, (401,403))

        token = self.auth()
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
        # create
        res = self.client.post("/api/bookings/", {
            "name":"Alice", "guests":2, "booking_date":"2030-01-01", "booking_time":"19:00", "special_requests":"window"
        }, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        bid = res.data["id"]

        # list (should see our own)
        res = self.client.get("/api/bookings/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

        # update own
        res = self.client.patch(f"/api/bookings/{bid}/", {"guests":3}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["guests"], 3)

        # delete own
        res = self.client.delete(f"/api/bookings/{bid}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
