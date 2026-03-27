from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # Jalur buat login Google
    path('', include('core.urls')),             # Jalur buat halaman utama biodata
]