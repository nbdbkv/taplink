from django.urls import path

from apps.templates_app.views import SignInView, RegistrationView, RegistrationNumberView, ChangePasswordView, \
    RegistrationSubmitView, EditProfileView, ChangeNumberSubmitView, ChangeNumberView, IndexView, ProductsView, \
    ShopView, ShopOwnerView, ShopInnerView, CartView, BoughtProductsView, CollectionView, BuyProductView, IndexGuestView

urlpatterns = [
    path('sign-in', SignInView.as_view(), name='sign-in_page'),
    path('registration', RegistrationView.as_view(), name='reg_page'),
    path('registration-number', RegistrationNumberView.as_view(), name='reg-number_page'),
    path('registration-submit', RegistrationSubmitView.as_view(), name='registration-submit_page'),
    path('edit-profile', EditProfileView.as_view(), name='edit-profile'),
    path('change-password', ChangePasswordView.as_view(), name='change-password_page'),
    path('change-number-submit', ChangeNumberSubmitView.as_view(), name='change-num-submit_page'),
    path('change-number', ChangeNumberView.as_view(), name='change-num_page'),
    path('', IndexView.as_view(), name='index_page'),
    path('products', ProductsView.as_view(), name='products'),
    path('shop', ShopView.as_view(), name='shop'),
    path('shop-owner', ShopOwnerView.as_view(), name='shop-owner'),
    path('shop-inner', ShopInnerView.as_view(), name='shop-inner'),
    path('cart', CartView.as_view(), name='cart'),
    path('bought-products', BoughtProductsView.as_view(), name='bought-products'),
    path('collection', CollectionView.as_view(), name='collection'),
    path('buy-product', BuyProductView.as_view(), name='buy-product'),
    path('index-guest', IndexGuestView.as_view(), name='index-guest'),
]
