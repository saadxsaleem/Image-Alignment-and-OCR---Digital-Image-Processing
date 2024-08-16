from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.upload, name='upload'),
    path('process_image/', views.process_image, name='process_image'),
    path('process_image/remove_shadow/', views.removeshad, name='removeshad'),
     path('process_image/ocr/', views.performOCR, name='perform_ocr'),
     path('process_image/brighten/', views.brightenImage, name='brightenImage'),
     path('process_image/saturateImage/', views.saturateImage, name='saturateImage'),
    path('download_text_file/', views.download_text_file, name='download_text_file'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
