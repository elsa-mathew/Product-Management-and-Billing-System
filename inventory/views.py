from django.shortcuts import render, redirect
from .models import Inventory
from products.models import Category

def inventory_page(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    # CHECK ROLE
    role = request.user.userprofile.role

    if role not in ['admin', 'manager']:
        return redirect('/login/')

    # STOCK UPDATE
    if request.GET.get('add'):
        inv = Inventory.objects.get(id=request.GET.get('add'))
        inv.quantity += 1
        inv.save()
        return redirect('/inventory/')

    if request.GET.get('remove'):
        inv = Inventory.objects.get(id=request.GET.get('remove'))

        if inv.quantity > 0:
            inv.quantity -= 1
            inv.save()

        return redirect('/inventory/')

    categories = Category.objects.all()

    data = []
    for cat in categories:
        items = Inventory.objects.filter(product__category=cat)
        data.append({
            'category': cat,
            'items': items
        })

    # CHOOSE TEMPLATE BASED ON ROLE
    template = 'inventory.html'

    if role == 'manager':
        template = 'manager_inventory.html'

    return render(request, template, {'data': data})