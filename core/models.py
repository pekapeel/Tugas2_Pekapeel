from django.db import models

class WebsiteConfig(models.Model):
    primary_color = models.CharField(max_length=7, default="#ffffff") # Simpan kode HEX warna
    font_family = models.CharField(max_length=50, default="Arial")

    def __str__(self):
        return "Konfigurasi Tampilan"