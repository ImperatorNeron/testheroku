from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from django.urls import re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls"), name="main"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
