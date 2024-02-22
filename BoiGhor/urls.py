from django.contrib import admin
from django.urls import path, include
from .views import HomeView, filterview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view(), name='home'),
    path("filter/<int:id>", filterview, name="filter"),
    path("account/", include("account.urls")),
    path("books/", include("book.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
