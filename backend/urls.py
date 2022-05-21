
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('kits/', include('base.urls')),
    path('api/', include('base.api.urls')),
    
]
