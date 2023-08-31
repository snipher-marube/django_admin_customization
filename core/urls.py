
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Django Admin Customization"
admin.site.site_title = "Django Admin Customization"
admin.site.index_title = "Welcome to Django Admin Customization Panel"

urlpatterns = [
    path("secretadmin/", admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
