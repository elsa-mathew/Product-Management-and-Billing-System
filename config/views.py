from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from products.models import Product
from inventory.models import Inventory
from billing.models import Bill


def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        user = authenticate(request, username=username, password=password)

        if user:
            # 🔥 ADMIN LOGIN (superuser only)
            if role == "admin":
                if user.is_superuser:
                    login(request, user)
                    return redirect('/dashboard/')
                else:
                    return render(request, 'login.html', {'error': 'Not an admin user'})

            # 🔥 MANAGER LOGIN
            elif role == "manager":
                if user.groups.filter(name='Manager').exists():
                    login(request, user)
                    return redirect('/inventory/')
                else:
                    return render(request, 'login.html', {'error': 'Not a manager'})

            # 🔥 STAFF LOGIN
            elif role == "staff":
                login(request, user)
                return redirect('/billing/')

            else:
                return render(request, 'login.html', {'error': 'Select a role'})

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