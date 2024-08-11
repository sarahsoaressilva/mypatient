from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from staffview.urls import *

urlpatterns = [
    path('', include('staffview.urls') ),
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
]

# Configuração para ver arquivos MEDIA em DEBUG TRUE
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
)
