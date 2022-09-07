from django.urls import path
from .views import SignUpView,LoginView, CheckAuthentication

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign up"),
    path("login/", LoginView.as_view(), name="login"),
    path("list-users/", CheckAuthentication.as_view(),name="check authentication")
]
