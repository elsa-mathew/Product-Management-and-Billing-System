from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login , logout
from products.models import Product , Category
from inventory.models import Inventory
from billing.models import Bill
from accounts.models import UserProfile
from django.utils.timezone import now


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
            
            try:
                profile = UserProfile.objects.get(user=user)
            except UserProfile.DoesNotExist:
                return render(request,'login.html' , {'error' : 'User role not assigned'})
            # MANAGER LOGIN
            if profile.role == "manager":
                return redirect('/manager/dashboard/')
               

            # STAFF LOGIN
            elif profile.role == "staff":
                return redirect('staff_dashboard')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def dashboard(request):
    total_products = Product.objects.count()
    total_users = UserProfile.objects.count()
    total_categories = Category.objects.count()

    # low stock (example logic)
    low_stock = Inventory.objects.filter(quantity__lt=5).count()

    return render(request, 'dashboard.html', {
        'total_products': total_products,
        'total_users': total_users,
        'total_categories': total_categories,
        'low_stock': low_stock
    })

def logout_view(request):
    logout(request)
    return redirect('/login/')

from inventory.models import Inventory

def manager_dashboard(request):

    total_products = Inventory.objects.count()
    low_stock = Inventory.objects.filter(quantity__lt=15, quantity__gt=0).count()
    out_stock = Inventory.objects.filter(quantity=0).count()

    return render(request, 'manager_dashboard.html', {
        'total_products': total_products,
        'low_stock': low_stock,
        'out_stock': out_stock
    })

def staff_dashboard(request):
    total_bills = Bill.objects.count()
    today_bills = Bill.objects.filter(created_at__date=now().date()).count()

    return render(request, 'staff_dashboard.html', {
        'total_bills': total_bills,
        'today_bills': today_bills
    })