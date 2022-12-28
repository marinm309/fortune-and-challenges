from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fortune/', views.fortune, name='fortune'),
    path('challenge/', views.challenge, name='challenge'),
    path('wheel/', views.wheel, name='wheel'),
]