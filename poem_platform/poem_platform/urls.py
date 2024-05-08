from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Adjust 'accounts' to match your app name
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # Other URL patterns
]
