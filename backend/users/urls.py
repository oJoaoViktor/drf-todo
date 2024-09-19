from django.urls import path, include

urlpatterns = [
    path('auth/', include('djoser.urls')),  # Endpoints para registro, login, etc.
    path('auth/', include('djoser.urls.jwt')),  # JWT endpoints (obter e refrescar tokens)
]
