from django.urls import path
from .views import user_management

urlpatterns = [
    path('', user_management),
]