from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from . import views

app_name = 'users'

urlpatterns = [
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
]