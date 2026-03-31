from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from products.models import Product
from inventory.models import Inventory
from billing.models import Bill
from accounts.models import UserProfile


def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # ADMIN LOGIN
            if user.is_superuser:
                return redirect('/dashboard/')
            
            profile = UserProfile.objects.get(user=user)   
            # MANAGER LOGIN
            if profile.role == "manager":
                return redirect('/inventory/')
               

            # STAFF LOGIN
            elif profile.role == "staff":
                return redirect('/billing/')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def dashboard(request):
    total_products = Product.objects.count()
    total_stock = sum([i.quantity for i in Inventory.objects.all()])
    total_bills = Bill.objects.count()
    total_revenue = sum([b.total_amount for b in Bill.objects.all()])

    return render(request, 'dashboard.html', {
        'total_products': total_products,
        'total_stock': total_stock,
        'total_bills': total_bills,
        'total_revenue': total_revenue
    })

def logout_view(request):
    logout(request)
    return redirect('/login/')