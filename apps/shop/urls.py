from django.urls import path

from apps.shop.views import (
    ProductsView, ProductAddFormView, ProductDeleteView, BoughtProductsView, CollectionView, ProductOwnerView,
    ShopOwnerView, add_collection_with_ajax
)


urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('add/', ProductAddFormView.as_view(), name='product-add'),
    path('add_collection/', add_collection_with_ajax, name='collection-add'),
    path('delete/<slug:slug>/', ProductDeleteView.as_view(), name='product-delete'),
    path('bought-products/', BoughtProductsView.as_view(), name='bought-products'),
    path('collection/', CollectionView.as_view(), name='collection'),
    path('<slug:shop_owner>/', ShopOwnerView.as_view(), name='shop-owner'),
    path('<slug:shop_owner>/<slug:product_owner>/', ProductOwnerView.as_view(), name='product-owner'),
]
