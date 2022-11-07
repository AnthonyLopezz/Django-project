from CartApp.cart import Cart
from StoreApp.models import Product
from django.shortcuts import redirect

# Create your views here.


def add_product(request, product_id):
    car = Cart(request)
    product = Product.objects.get(id=product_id)
    car.add(product=product)

    return redirect("Cart")


def delete_product(request, product_id):
    car = Cart(request)
    product = Product.objects.get(id=product_id)
    car.delete(product=product)

    return redirect("Cart")


def rest_product(request, product_id):
    car = Cart(request)
    product = Product.objects.get(id=product_id)
    car.rest_product(product=product)

    return redirect("Cart")


def empty_car(request):
    car = Cart(request)
    car.empty_car()
    return redirect("Cart")
