from CartApp.cart import Cart


def import_total_cart(request):
    cart = Cart(request)
    total = 0
    if not request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total = total + (float(value["price"]) * value["quantity"])

    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            total = total + (float(value["price"]) * value["quantity"])
    return {"import_total_cart": total}


def import_sum_cart(request):
    cart = Cart(request)
    items = 0
    if not request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            items = items + value["quantity"]

    if request.user.is_authenticated:
        for key, value in request.session["cart"].items():
            items = items + value["quantity"]
    return {"import_sum_cart": items}

