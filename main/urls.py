from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fortune/', views.fortune, name='fortune'),
    path('challenge/', views.challenge, name='challenge'),
    path('wheel/', views.wheel, name='wheel'),
    path('update_customer_credits/', views.update_customer_credits, name='update_customer_credits'),
]