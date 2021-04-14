from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

<<<<<<< HEAD
    path('', include('apps.users.urls')),
=======
    path('templates/', include('apps.templates_app.urls')),
>>>>>>> fe759124b250b6ed89b3c3ce0ed0ce91386ac312
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
