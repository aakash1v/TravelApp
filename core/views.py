from django.shortcuts import render, redirect
from booking.models import TravelOption
from .forms import SignupForm


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


def dashboard(req):
    travel_options = TravelOption.objects.all()
    return render(req, 'core/dashboard.html', {'travel_options': travel_options})


def travel_details(req, type):
    travel_option = TravelOption.objects.filter(type=type).first()
    print(travel_option, type)

    return render(req, 'core/travel_details.html',
                  {'travel_medium': type, 'travel_option': travel_option})
