from django.shortcuts import render, redirect
from .models import Category, Product

def product_management(request):

    error = ""

    # 👉 DELETE CATEGORY
    if request.GET.get('delete_category'):
        cat_id = request.GET.get('delete_category')
        Category.objects.filter(id=cat_id).delete()
        return redirect('/products/')

    if request.method == "POST":

        # 👉 CATEGORY ADD
        if request.POST.get('category_name') is not None:
            name = request.POST.get('category_name')

            if not name:
                error = "Category name cannot be empty"
            else:
                Category.objects.create(name=name)
                return redirect('/products/')

        # 👉 PRODUCT ADD
        elif request.POST.get('product_name') is not None:
            name = request.POST.get('product_name')
            price = request.POST.get('price')
            category_id = request.POST.get('category')

    # 🔥 VALIDATION
            if not name:
                error = "Product name cannot be empty"

            elif not price:
                error = "Price cannot be empty"

            elif not category_id:
                error = "Please select a category"

            elif float(price) <= 0:
                error = "Price must be greater than 0"

            else:
                # ✅ CHECK DUPLICATE (optional but good)
                if Product.objects.filter(name=name).exists():
                    error = "Product already exists"
                else:
                    category = Category.objects.get(id=category_id)

                    Product.objects.create(
                        name=name,
                        price=price,
                        category=category
                    )

                    return redirect('/products/')
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'product_management.html', {
        'categories': categories,
        'products': products,
        'error': error
    })