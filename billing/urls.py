from django.urls import path
from .views import billing_view , generate_bill , bill_detail , bill_view_page

urlpatterns = [
    path('', billing_view),
    path('generate/', generate_bill),
    path ('details/', bill_detail),
    path('view/<int:bill_id>/', bill_view_page),
]