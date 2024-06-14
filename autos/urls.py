# autos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_marca/', views.crear_marca, name='crear_marca'),
    path('crear_auto/', views.crear_auto, name='crear_auto'),
]


