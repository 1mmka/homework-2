from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import NewFile,PrintedFile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',NewFile.as_view(),name='create_file'),
    path('printed_files',PrintedFile.as_view(),name='list_files')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
