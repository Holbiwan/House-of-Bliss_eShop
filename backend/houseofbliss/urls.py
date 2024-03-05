from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'^manifest\.json$', serve, {
        'path': 'manifest.json',
        'document_root': settings.FRONTEND_BUILD_DIR
    }),

    re_path(r'^favicon\.ico$', serve, {
        'path': 'favicon.ico',
        'document_root': settings.FRONTEND_BUILD_DIR
    }),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
