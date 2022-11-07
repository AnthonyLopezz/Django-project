class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product):
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "category": product.category,
                "description": product.description,
                "price": str(product.price),
                "quantity": 1,
                "image": product.image.url
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    value["quantity"] = value["quantity"] + 1
                    break
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def rest_product(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value["quantity"] - 1
                if value["quantity"] < 1:
                    self.delete(product)
                else:
                    self.save()
                break
        self.save()

    def empty_car(self):
        self.session["cart"] = {}
        self.session.modified = True
