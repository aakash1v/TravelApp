from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("travel-details/<str:type>", views.travel_details, name="travel_details"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html",
                                                authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="core:home"), name="logout"),
]
