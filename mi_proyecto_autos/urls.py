# mi_proyecto_autos/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autos/', include('autos.urls')),
    path('', include('autos.urls')),
]

