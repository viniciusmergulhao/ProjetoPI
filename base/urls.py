from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('', Home, 'nome rota'),
    path('about', )
]
