from django.shortcuts import render, redirect
from .models import Category, Product
from inventory.models import Inventory

def product_management(request):

    error = ""

    # DELETE LOGIC 
    if request.GET.get('delete_product'):
        product_id = request.GET.get('delete_product')

        product = Product.objects.get(id=product_id)

        # delete inventory first
        Inventory.objects.filter(product=product).delete()

        # delete product
        product.delete()

        return redirect('/products/')

    # 🔥 2. POST LOGIC (ADD CATEGORY / PRODUCT)
    if request.method == "POST":

        # CATEGORY ADD
        if request.POST.get('category_name'):
            name = request.POST.get('category_name')

            if not name:
                error = "Category name cannot be empty"
            else:
                Category.objects.create(name=name)
                return redirect('/products/')

        # PRODUCT ADD
        elif request.POST.get('product_name'):
            name = request.POST.get('product_name')
            price = request.POST.get('price')
            category_id = request.POST.get('category')

            if not name or not price or not category_id:
                error = "All fields required"
            else:
                category = Category.objects.get(id=category_id)

                product = Product.objects.create(
                    name=name,
                    price=price,
                    category=category
                )

                Inventory.objects.create(product=product, quantity=0)

                return redirect('/products/')

    # 🔥 3. FETCH DATA (LAST)
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'product_management.html', {
        'categories': categories,
        'products': products,
        'error': error
    })