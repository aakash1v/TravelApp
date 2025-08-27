from django.urls import path
from . import views

app_name = "booking"

urlpatterns = [
    path("", views.get_all_bookings, name="bookings")
]
