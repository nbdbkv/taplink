from django.urls import path

from apps.shop.views import (
    ProductListView, ProductDetailView, CartView, ShopView, ProductsSoldView,
    ProductAddFormView, ProductDeleteView, ProductCollectionListView
)


urlpatterns = [
    path('add/', ProductAddFormView.as_view(), name='product-add_page'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='product-delete_page'),
    path('<slug:slug>/detail/', ProductDetailView.as_view(), name='product-detail_page'),
    path('products_sold/', ProductsSoldView.as_view(), name='products-sold_page'),
    path('cart/', CartView.as_view(), name='cart_page'),
    path('products/', ProductListView.as_view(), name='products_page'),
    path('<slug:pathname>/<slug:slug>/', ProductCollectionListView.as_view(), name='collection_page'),
    path('<slug:pathname>/', ShopView.as_view(), name='shop_page'),
]
