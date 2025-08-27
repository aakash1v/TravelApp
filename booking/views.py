from asyncio import wait
from django.http import JsonResponse
from django.shortcuts import render

"""
we have two options to convert model obj to json --> 
1. from django.forms.models import model_to_dict
2. use list on model_list_obj.values()
"""
from .models import Booking, TravelOption


def get_travel_list(req):
    travel_list = list(TravelOption.objects.all().values())
    return JsonResponse({
        'travel_list': travel_list
    })


def get_all_bookings(req):
    bookings = Booking.objects.filter(customer=req.user)
    return render(req, 'booking/index.html', {'bookings': bookings})


