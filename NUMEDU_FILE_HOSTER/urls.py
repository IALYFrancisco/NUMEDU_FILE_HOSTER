from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from images.views import UploadedImageViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'images', UploadedImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# Pour servir les fichiers en dev
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)