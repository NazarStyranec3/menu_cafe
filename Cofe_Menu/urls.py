from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import os
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # приклад твоїх app урлів
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'main', 'static'))
