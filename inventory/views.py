from django.shortcuts import render, redirect
from .models import Inventory
from products.models import Category

def inventory_page(request):

    # 🔥 UPDATE STOCK
    if request.GET.get('add'):
        inv_id = request.GET.get('add')
        inventory = Inventory.objects.get(id=inv_id)
        inventory.quantity += 1
        inventory.save()
        return redirect('/inventory/')

    if request.GET.get('remove'):
        inv_id = request.GET.get('remove')
        inventory = Inventory.objects.get(id=inv_id)

        # ❗ PREVENT NEGATIVE
        if inventory.quantity > 0:
            inventory.quantity -= 1
            inventory.save()

        return redirect('/inventory/')

    # 🔥 GROUP BY CATEGORY
    categories = Category.objects.all()

    data = []
    for cat in categories:
        items = Inventory.objects.filter(product__category=cat)
        data.append({
            'category': cat,
            'items': items
        })

    return render(request, 'inventory.html', {
        'data': data
    })