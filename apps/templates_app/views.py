from django.views.generic import TemplateView


class SignInView(TemplateView):
    template_name = 'pages/sign-in.html'


class RegistrationView(TemplateView):
    template_name = 'pages/registration.html'


class RegistrationNumberView(TemplateView):
    template_name = 'pages/registration-number.html'


class RegistrationSubmitView(TemplateView):
    template_name = 'pages/registration-submit.html'


class EditProfileView(TemplateView):
    template_name = 'pages/edit-profile.html'


class ChangePasswordView(TemplateView):
    template_name = 'pages/change-password.html'


class ChangeNumberSubmitView(TemplateView):
    template_name = 'pages/change-number-submit.html'


class ChangeNumberView(TemplateView):
    template_name = 'pages/change-number.html'


class IndexView(TemplateView):
    template_name = 'pages/index.html'


class ProductsView(TemplateView):
    template_name = 'pages/shop/products.html'


class ShopView(TemplateView):
    template_name = 'pages/customer/shop-customer.html'


class ShopOwnerView(TemplateView):
    template_name = 'pages/shop/shop-owner.html'


class ShopInnerView(TemplateView):
    template_name = 'pages/customer/product-customer.html'


class CartView(TemplateView):
    template_name = 'pages/customer/cart.html'


class BoughtProductsView(TemplateView):
    template_name = 'pages/shop/bought-products.html'


class CollectionView(TemplateView):
    template_name = 'pages/shop/collection.html'


class BuyProductView(TemplateView):
    template_name = 'pages/customer/buy-product.html'


class IndexGuestView(TemplateView):
    template_name = 'pages/customer/index-customer.html'
