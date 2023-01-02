from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fortune/', views.fortune, name='fortune'),
    path('challenge/', views.challenge, name='challenge'),
    path('wheel/', views.wheel, name='wheel'),
    path('update_customer_credits/', views.update_customer_credits, name='update_customer_credits'),
    path('update_customer_is_wheel_available/', views.update_customer_is_wheel_available, name='update_customer_is_wheel_available'),
    path('reset_at_midnight/', views.reset_at_midnight, name='reset_at_midnight'),
]