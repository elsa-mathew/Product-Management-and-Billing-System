from django.shortcuts import render, redirect
from .models import Inventory
from products.models import Category

def inventory_page(request):

    if not request.user.is_authenticated:                             #validating user profile becuase only admin and manager can use this page
        return redirect('/login/')
    profile = getattr(request.user, 'userprofile', None)              #helps to avoid crashing during validation because admin(super user) is not listed in the user profile table . 
                                                                      #so when we call (request.user.userprofile) system didnt recognise admin and cause crash.
                                                                      #here we used (None) . So even if table have no admin the profile value will be none. And system understand its the superuser admin.
    if request.user.is_superuser:
        role = 'admin'
    else:
        role = profile.role
    if role not in ['admin', 'manager']:
        return redirect('/login/')

    if request.GET.get('add'):                                          #update stock in inventory by 10
        inventory = Inventory.objects.get(id=request.GET.get('add'))
        inventory.quantity += 10                                         #increase stock by 10 count
        inventory.save()
        return redirect('/inventory/')

    if request.GET.get('remove'):                                       #remove stock in inventory by 1
        inventory = Inventory.objects.get(id=request.GET.get('remove'))

        if inventory.quantity > 0:
            inventory.quantity -= 1                                     #reduce stock by 1 count
            inventory.save()

        return redirect('/inventory/')

    categories = Category.objects.all()

    data = []
    for category in categories:
        items = Inventory.objects.filter(product__category_id=category.id)
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
        data.append({                                          #appending products category wise
            'category': category,
            'items': item_list
        })

    
    template = 'inventory.html'

    if role == 'manager':
        template = 'manager_inventory.html'

    return render(request, template, {'data': data})