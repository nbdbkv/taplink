import requests
import xml.etree.ElementTree as ET

from loguru import logger

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView

from apps.customer.cart import Cart
from apps.customer.choices import CASH, ONLINE
from apps.customer.forms import OrderForm
from apps.customer.models import Order, OrderItem
from apps.customer.paybox_services import PayboxPaymentService
from apps.shop.models import Product, ProductImage
from apps.taplink.models import TapLink


paybox_service = PayboxPaymentService()


class IndexCustomerView(TemplateView):
    template_name = 'pages/customer/index-customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taplink'] = TapLink.objects.filter(pathname=self.kwargs['shop_customer'])\
            .prefetch_related('messengers').prefetch_related('editors')
        return context


class ShopCustomerView(ListView):
    model = Product
    template_name = 'pages/customer/shop-customer.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.request.GET.get('search'):
            return Product.objects.filter(
                Q(name__icontains=self.request.GET.get('search')) &
                Q(owner__pathname=self.kwargs['shop_customer']) &
                Q(is_available=True)
            )
        else:
            return Product.objects.filter(
                Q(owner__pathname=self.kwargs['shop_customer']) &
                Q(is_available=True)
            )


class ProductCustomerView(DetailView):
    model = Product
    template_name = 'pages/customer/product-customer.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductImage.objects.filter(product=self.object)
        return context


class ProductAddToCartView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug, is_available=True)
        cart.add(product=product)
        print(request, args, kwargs)
        return redirect(product.owner.get_absolute_url_for_customer())


class ProductRemoveFromCartView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug, is_available=True)
        cart.remove(product=product)
        return redirect('cart')


class ProductDecreaseView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug, is_available=True)
        cart.decrease(product=product)
        return redirect('cart')


class ProductIncreaseView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        slug = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug, is_available=True)
        cart.increase(product=product)
        return redirect('cart')


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'pages/customer/cart.html', {'cart': cart})


class OrderFormView(FormView):
    model = Order
    form_class = OrderForm
    template_name = 'pages/customer/buy-product.html'

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        order_items = []
        for item in cart:
            order_item = OrderItem(
                product_owner=item['product'].owner, order=order, product=item['product'],
                price=item['price'], quantity=item['quantity']
            )
            order_items.append(order_item)
            product = item['product']
            product.quantity -= item['quantity']
            if product.quantity == 0:
                product.is_available = False
            product.save()
        OrderItem.objects.bulk_create(order_items)
        cart.clear()
        if order.payment_method == CASH:
            messages.add_message(self.request, messages.INFO, 'Thank you for your purchase!')
            return redirect('cart')
        elif order.payment_method == ONLINE:
            response = requests.get(paybox_service.get_payment_body(order, self.request))
            root = ET.fromstring(response.text)
            payment_url = root.find('pg_redirect_url').text
            return redirect(payment_url)
        return redirect('cart')


class GetPaymentResponse(View):
    def get(self, request):
        result = request.GET.get('pg_result')
        order_id = request.GET.get('pg_order_id')
        if not order_id:
            raise PermissionDenied('Order is not found')
        if result:
            order = Order.objects.filter(id=order_id).update(is_paid=True)
        else:
            logger.warning(f'Something went wrong. Please check the {order_id} order')
        return HttpResponse(result)
