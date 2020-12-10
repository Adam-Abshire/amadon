from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all(),
    }
    return render(request, "store/index.html", context)

def checkout(request):
    new_total = 0
    total_charge = Order.objects.last().total_price
    number_of_orders = len(Order.objects.all())
    total_history = Order.objects.all()
    for total in total_history:
        new_total = total.total_price + new_total
    context = {
        'price' : total_charge,
        'items' : number_of_orders,
        'total' : new_total,
    }
    return render(request, "store/checkout.html", context)

def purchase(request):
    quantity_from_form = int(request.POST["quantity"])
    id_from_form = Product.objects.get(id=request.POST["id"])
    price_from_form = id_from_form.price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout')