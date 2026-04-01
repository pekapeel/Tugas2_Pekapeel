from django.shortcuts import render, redirect
from django.conf import settings
from .models import WebsiteConfig
from django.contrib.auth import logout
from django.contrib import messages

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

# validasi input saat ganti warna atau font
def update_style(request):
    # SECURITY CHECK: Hanya izinkan POST dan Anggota Kelompok
    if request.method == 'POST' and request.user.is_authenticated:
        if request.user.email in settings.ALLOWED_GROUP_MEMBERS:
            allowed_fonts = [
                'Arial', 'Courier New', 'Georgia', 'DM Sans', 
                'DM Serif Display', 'Lora', 'Playfair Display', 
                'Space Mono', 'Fraunces'
            ]
            selected_font = request.POST.get('font')

            if selected_font in allowed_fonts:
                config = WebsiteConfig.objects.get(id=1)
                config.primary_color = request.POST.get('color')
                config.font_family = selected_font
                config.save()
    return redirect('home')

# logout karena session
def force_logout(request):
    logout(request)
    messages.info(request, "You have signed out because the session is out")
    return redirect('home')