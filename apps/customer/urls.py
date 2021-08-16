from django.urls import path

from apps.customer.views import (
    OrderFormView, CartView, ProductCustomerView, ShopCustomerView,
    IndexCustomerView, ProductAddToCartView, ProductIncreaseView,
    ProductDecreaseView, ProductRemoveFromCartView, GetPaymentResponse
)


urlpatterns = [
    path('buy-product/', OrderFormView.as_view(), name='buy-product'),
    path('paybox-order/', GetPaymentResponse.as_view(), name='get_payment_response'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add/<slug:slug>/', ProductAddToCartView.as_view(), name='cart_add'),
    path('remove/<slug:slug>/', ProductRemoveFromCartView.as_view(), name='cart_remove'),
    path('decrease/<slug:slug>/', ProductDecreaseView.as_view(), name='product_decrease'),
    path('increase/<slug:slug>/', ProductIncreaseView.as_view(), name='product_increase'),
    path('shop/<slug:shop_customer>/', ShopCustomerView.as_view(), name='shop-customer'),
    path('<slug:shop_customer>/', IndexCustomerView.as_view(), name='index-customer'),
    path('shop/<slug:shop_customer>/<slug:product_customer>/', ProductCustomerView.as_view(), name='product-customer'),
]
