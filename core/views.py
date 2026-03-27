from django.shortcuts import render, redirect
from django.conf import settings
from .models import WebsiteConfig

def home(request):
    # Ambil konfigurasi tampilan pertama (atau buat jika belum ada)
    config, created = WebsiteConfig.objects.get_or_create(id=1)
    
    # Cek apakah user adalah anggota kelompok
    is_member = False
    if request.user.is_authenticated:
        if request.user.email in settings.ALLOWED_GROUP_MEMBERS:
            is_member = True
            
    context = {
        'config': config,
        'is_member': is_member,
    }
    return render(request, 'index.html', context)

def update_style(request):
    # SECURITY CHECK: Hanya izinkan POST dan Anggota Kelompok
    if request.method == 'POST' and request.user.is_authenticated:
        if request.user.email in settings.ALLOWED_GROUP_MEMBERS:
            config = WebsiteConfig.objects.get(id=1)
            config.primary_color = request.POST.get('color')
            config.font_family = request.POST.get('font')
            config.save()
            
    return redirect('home')