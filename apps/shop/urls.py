from django.urls import path

from apps.shop.views import ShopView

urlpatterns = [
    path('', ShopView.as_view(), name='shop-index_page'),
]
