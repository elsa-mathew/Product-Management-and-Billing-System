from django.urls import path
from . import views
from .views import product_management , view_categories

urlpatterns = [
    path('', product_management),
    path('categories/', views.view_categories, name='view_categories'),
    path('view/', views.view_products, name='view_products'),
]