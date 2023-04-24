from django.urls import path

from accounts.views import (
    PasswordResetView,
    UserLoginView,
    UserPasswordChangeView,
    UserPasswordResetView,
    UserProfileView,
    UserRegiatrationView,
)

urlpatterns = [
    path(
        "register/", UserRegiatrationView.as_view(), name="register"
    ),  # Registation of user
    path("login/", UserLoginView.as_view(), name="UserLogin"),  # User Login
    path("profile/", UserProfileView.as_view(), name="user_view"),  # Profile View
    path(
        "changepassword/", UserPasswordChangeView.as_view(), name="user_password_change"
    ),  # Password Change
    path(
        "send_reset_password_email/",
        PasswordResetView.as_view(),
        name="user_password_reset",
    ),  # Passowrd Reset
    path(
        "user_password_reset/<uid>/<token>/",
        UserPasswordResetView.as_view(),
        name="user_password_reset",
    ),  # PPassword reset token send
]
