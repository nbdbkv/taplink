from django.urls import path

from apps.shop.views import (
    ProductsView, ProductAddFormView, ProductDeleteView, BoughtProductsView,
    CollectionView, ShopOwnerView, BuyProductView, CartView, ShopInnerView,
    ShopCustomerView, IndexCustomerView, add_collection_with_ajax
)


urlpatterns = [
    # Owner
    path('products/', ProductsView.as_view(), name='products'),
    path('add/', ProductAddFormView.as_view(), name='product-add'),
    path('add_collection/', add_collection_with_ajax, name='collection-add'),
    path('delete/<slug:slug>/', ProductDeleteView.as_view(), name='product-delete'),
    path('bought-products/', BoughtProductsView.as_view(), name='bought-products'),
    path('collection/', CollectionView.as_view(), name='collection'),
    path('<slug:pathname>/', ShopOwnerView.as_view(), name='shop-owner'),

    # Customer
    path('customer/buy-product/', BuyProductView.as_view(), name='buy-product'),
    path('customer/cart/', CartView.as_view(), name='cart'),
    path('customer/shop/<slug:pathname>/<slug:product_slug>/', ShopInnerView.as_view(), name='shop-inner'),
    path('customer/shop/<slug:pathname>/', ShopCustomerView.as_view(), name='shop'),
    path('customer/<slug:pathname>/', IndexCustomerView.as_view(), name='index-customer'),
]
