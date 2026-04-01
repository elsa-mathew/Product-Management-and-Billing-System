from django.urls import path
from .views import billing_view , generate_bill , bill_detail , bill_view_page

urlpatterns = [
    path('', billing_view , name='billing'),
    path('generate/', generate_bill , name='generate_bill'),
    path ('details/', bill_detail , name='bill_history'),
    path('view/<int:bill_id>/', bill_view_page),
]