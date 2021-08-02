from decimal import Decimal
from django.conf import settings
from apps.shop.models import Product


class Cart(object):

    def __init__(self, request):
        """Initialize the cart."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        # Save an empty cart in the session
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """Add a product to the cart or update its quantity."""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.current_price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Mark the session as "modified" to make sure it gets saved."""
        self.session.modified = True

    def increase(self, product, quantity=1, update_quantity=False):
        """Increase a product quantity from the cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def decrease(self, product, quantity=1, update_quantity=False):
        """Decrease a product quantity from the cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] -= quantity
        self.save()

    def remove(self, product):
        """Remove a product from the cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Iterate over the items in the cart and get the products from the database."""
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Count all items in the cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_quantity(self):
        """Count total quantity of all items in the cart."""
        return len(self.cart)

    def get_total_price(self):
        """Count total price of all items in the cart."""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Remove cart from session."""
        del self.session[settings.CART_SESSION_ID]
        self.save()
