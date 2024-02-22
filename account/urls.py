from django.urls import path
from .views import RegisterView, user_logout, UserLoginView, BorrowView, ProfileView, ReturnView, DepositView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", user_logout, name="logout"),
    path("borrow/<int:id>", BorrowView.as_view(), name="borrow"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("return/<int:id>", ReturnView.as_view(), name="return"),
    path("deposit", DepositView.as_view(), name="deposit"),
]
