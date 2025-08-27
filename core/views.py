from django.contrib.auth.forms import User
from django.contrib.auth.views import login_required
from django.shortcuts import get_object_or_404, render, redirect
from booking.models import TravelOption
from .forms import BookingForm, SignupForm, TravelSearchForm
from django.contrib.auth.views import login_required


def signup(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(req, 'core/signup.html',
                  {'form': form})


def index(req):
    return render(req, 'core/base.html')


def account(req):
    form = SignupForm(instance=req.user)
    return render(req, 'core/account.html', {'form': form})


@login_required
def dashboard(req):
    travel_options = TravelOption.objects.all()
    return render(req, 'core/dashboard.html', {'travel_options': travel_options})


def travel_search(req, type):
    form = TravelSearchForm(req.GET or None)
    travels = None

    if form.is_valid():
        source = form.cleaned_data["source"]
        destination = form.cleaned_data["destination"]
        travels = TravelOption.objects.filter(
            source__icontains=source,
            destination__icontains=destination,
            type=type
        )

    # ✅ Get unique values for dropdown
    sources = TravelOption.objects.values_list("source", flat=True).distinct()
    destinations = TravelOption.objects.values_list(
        "destination", flat=True).distinct()

    return render(req, "core/travel_search.html", {
        "travel_type": type,
        "travels": travels,
        "form": form,
        "sources": sources,
        "destinations": destinations,
    })


@login_required
def travel_booking(req, travel_id):
    travel = get_object_or_404(TravelOption, id=travel_id)

    if req.method == "POST":
        form = BookingForm(req.POST)
        if form.is_valid():
            booking = form.save(commit=False)   # don't save yet
            booking.customer = req.user         # ✅ set logged-in user
            booking.travel_option = travel      # ✅ set travel option
            booking.total_price = (
                booking.number_of_seats * travel.price
            )                                   # ✅ calculate total
            booking.save()

            # Reduce available seats
            travel.available_seats -= booking.number_of_seats
            travel.save()

            # redirect to a bookings list page
            return redirect("booking:bookings")
    else:
        form = BookingForm()

    return render(req, "core/travel_booking.html", {
        "form": form,
        "travel": travel,
    })
