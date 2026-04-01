from django.shortcuts import render, redirect
from .models import Category, Product
from inventory.models import Inventory
from django.contrib import messages

def product_management(request):

    categories = Category.objects.all()
    error = ""

    if request.method == "POST":

        # CATEGORY ADD
        if request.POST.get('category_name'):
            name = request.POST.get('category_name')

            if name:
                if Category.objects.filter(name__iexact=name).exists():
                    messages.error(request,"Category already exists...")
                else:
                    Category.objects.create(name=name)
                    messages.success(request,"Category added Successfully")
            
            return redirect("/products/")
               
        elif request.POST.get('product_name'):
            name = request.POST.get('product_name')
            price = request.POST.get('price')
            category_id = request.POST.get('category')
            sku = request.POST.get('sku').upper()

            if not name or not price or not category_id or not sku:
                messages.error(request , "All fields required")
            else:
                category = Category.objects.get(id=category_id)

                if Product.objects.filter(sku=sku).exists():
                    messages.error(request , "SKU already exists")
                    
                else:

                    product = Product.objects.create(
                        name=name,
                        price=price,
                        category=category,
                        sku=sku
                    )

                    Inventory.objects.create(product=product, quantity=0)
                    messages.success(request,"Product added Successfully")
                    return redirect('/products/')

    products = Product.objects.all()

    return render(request, 'product_management.html', {
        'categories': categories,
        'products': products
    })


def view_categories(request):

    delete_id = request.GET.get('delete')
    if delete_id:
        Product.objects.filter(category_id=delete_id).delete()
        Category.objects.filter(id=delete_id).delete()
        return redirect('/products/categories/')

    categories = Category.objects.all()

    return render(request, 'view_categories.html', {
        'categories': categories
    })

def view_products(request):
    
    delete_id = request.GET.get('delete')
    if delete_id:
        Inventory.objects.filter(product_id=delete_id).delete()
        Product.objects.filter(id=delete_id).delete()
        return redirect('/products/view/')
    products = Product.objects.all()

    return render(request, 'view_products.html', {
        'products': products
    })