from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update-style/', views.update_style, name='update_style'),
]