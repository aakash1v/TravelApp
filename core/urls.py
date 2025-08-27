from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . forms import LoginForm

app_name = "core"

urlpatterns = [
    path("", views.index, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("travel-search/<str:type>", views.travel_search, name="travel_search"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html",
                                                authentication_form=LoginForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="core:home"), name="logout"),
    path("account/", views.account, name="account"),
    path("book/<int:travel_id>/", views.travel_booking, name="book_travel"),

]
