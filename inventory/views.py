from django.shortcuts import render, redirect
from .models import Inventory
from products.models import Category

def inventory_page(request):

    if not request.user.is_authenticated:
        return redirect('/login/')
    profile = getattr(request.user, 'userprofile', None)
    if request.user.is_superuser:
        role = 'admin'
    else:
        role = profile.role
    if role not in ['admin', 'manager']:
        return redirect('/login/')

    if request.GET.get('add'):                                          #update stock in inventory by 10
        inventory = Inventory.objects.get(id=request.GET.get('add'))
        inventory.quantity += 10
        inventory.save()
        return redirect('/inventory/')

    if request.GET.get('remove'):                                       #remove stock in inventory by 1
        inventory = Inventory.objects.get(id=request.GET.get('remove'))

        if inventory.quantity > 0:
            inventory.quantity -= 1
            inventory.save()

        return redirect('/inventory/')

    categories = Category.objects.all()

    data = []
    for cat in categories:
        items = Inventory.objects.filter(product__category_id=cat.id)
        item_list = []

        for item in items:
            quantity = item.quantity

            if quantity < 5:
                status = "Out of Stock"
            elif quantity < 15:
                status = "Low Stock"
            else:
                status = "In Stock"

            item_list.append({
                'object' : item,
                'status' : status
            })
        data.append({
            'category': cat,
            'items': item_list
        })

    
    template = 'inventory.html'

    if role == 'manager':
        template = 'manager_inventory.html'

    return render(request, template, {'data': data})