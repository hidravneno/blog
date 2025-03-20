from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),  # Home y About
    path('posts/', include('posts.urls')),  # CRUD de posts
    path('accounts/', include('accounts.urls')),  # Rutas personalizadas para registro
    path('accounts/', include('django.contrib.auth.urls')),  # Autenticación de Django
]
