from django.urls import path, include  # 'path' replaces 'url'
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('computers.urls')),
]