from django.urls import path

from apps.shop.views import (
    ProductsView, ProductDetailView, ProductsSoldView, ProductAddFormView,
    ProductDeleteView, ProductCollectionListView, ShopView,
    ShopOwnerView, ShopInnerView, CartView, BoughtProductsView, CollectionView,
    BuyProductView
)


urlpatterns = [
    path('add/', ProductAddFormView.as_view(), name='product-add_page'),
    path('<slug:slug>/delete/', ProductDeleteView.as_view(), name='product-delete_page'),
    path('<slug:slug>/detail/', ProductDetailView.as_view(), name='product-detail_page'),
    # path('products_sold/', ProductsSoldView.as_view(), name='products-sold_page'),
    # path('cart/', CartView.as_view(), name='cart_page'),
    # path('products/', ProductListView.as_view(), name='products_page'),
    # path('<slug:pathname>/<slug:slug>/', ProductCollectionListView.as_view(), name='collection_page'),
    # path('<slug:pathname>/', ShopView.as_view(), name='shop_page'),
    path('products/', ProductsView.as_view(), name='products'),
    path('shop/<slug:pathname>/', ShopView.as_view(), name='shop'),
    path('shop-owner/', ShopOwnerView.as_view(), name='shop-owner'),
    path('shop-inner/', ShopInnerView.as_view(), name='shop-inner'),
    path('cart/', CartView.as_view(), name='cart'),
    path('bought-products/', BoughtProductsView.as_view(), name='bought-products'),
    path('collection/', CollectionView.as_view(), name='collection'),
    path('buy-product/', BuyProductView.as_view(), name='buy-product'),
]
