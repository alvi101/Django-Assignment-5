from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path("detail/<int:pk>", BookDetailView.as_view(), name="detail"),
]
