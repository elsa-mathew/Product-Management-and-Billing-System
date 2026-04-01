from django.shortcuts import render, redirect
from .models import Bill, BillItem
from products.models import Product
from django.contrib import messages


def billing_view(request):

    #GET OR CREATE CURRENT BILL
    bill_id = request.session.get('bill_id')

    if not bill_id:
        bill = Bill.objects.create(created_by=request.user)
        request.session['bill_id'] = bill.id
    else:
        bill = Bill.objects.get(id=bill_id)

    # ADD PRODUCT
    if request.method == "POST":
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')

        if not product_id or not quantity:
            return redirect('/billing/')

        try:
            quantity = int(quantity)
        except:
            return redirect('/billing/')

        if quantity <= 0:
            return redirect('/billing/')

        product = Product.objects.get(id=product_id)

        # PREVENT DUPLICATE → UPDATE QUANTITY
        existing_item = BillItem.objects.filter(
            bill=bill,
            product=product
        ).first()

        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            BillItem.objects.create(
                bill=bill,
                product=product,
                quantity=quantity,
                price=product.price
            )

        return redirect('/billing/')

    # ITEMS
    items = BillItem.objects.filter(bill=bill)

    for item in items:
        item.total = item.quantity * item.price

    #TOTAL
    total = sum(item.quantity * item.price for item in items)

    return render(request, 'billing.html', {
        'bill': bill,
        'items': items,
        'products': Product.objects.all(),
        'total': total
    })

def generate_bill(request):
    bill_id = request.session.get('bill_id')

    if not bill_id:
        return redirect('/billing/')

    bill = Bill.objects.get(id=bill_id)

    
    items = BillItem.objects.filter(bill=bill)

    if not items.exists():
        messages.error(request, "Please select at least one product before generating bill.")
        return redirect('/billing/')

   
    del request.session['bill_id']

    return redirect('bill_history')

def bill_detail(request):
    bills = Bill.objects.all().order_by('-id')

    base_template = 'admin_base.html' if request.user.is_superuser else 'staff_base.html'

    for bill in bills:
        items = BillItem.objects.filter(bill=bill)
        total = sum(item.quantity * item.price for item in items)
        bill.total = total
        bill.save()

    return render(request, 'bill_details.html', {
        'bills': bills,
        'base_template': base_template
    })


def bill_view_page(request, bill_id):
    bill = Bill.objects.get(id=bill_id)

    items = BillItem.objects.filter(bill=bill)

    for item in items:
        item.total = item.quantity * item.price

    total = sum(item.total for item in items)
    base_template = 'admin_base.html' if request.user.is_superuser else 'staff_base.html'
    role = 'admin' if request.user.is_superuser else request.user.userprofile.role

    return render(request, 'bill_view.html', {
        'bill': bill,
        'items': items,
        'total': total,
        'base_template': base_template,
        'role' : role
    })