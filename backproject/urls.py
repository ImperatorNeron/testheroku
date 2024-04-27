from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from backproject.settings import DEBUG
from backproject import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls"), name="main"),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
