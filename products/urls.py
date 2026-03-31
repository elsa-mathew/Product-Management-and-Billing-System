from django.urls import path
from .views import product_management

urlpatterns = [
    path('', product_management),
]