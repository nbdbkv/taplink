from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, FormView, ListView, DetailView, DeleteView
)
from loguru import logger

from apps.shop.forms import ProductForm, ProductImageForm
from apps.shop.models import Product, ProductImage, Collection
from apps.taplink.models import TapLink


# Owner
class ProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'pages/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.request.GET.get('search'):
            return Product.objects.filter(
                Q(name__icontains=self.request.GET.get('search')) &
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            )
        else:
            return Product.objects.filter(
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = ProductForm
        context['image_form'] = ProductImageForm
        context['collections'] = Collection.objects.filter()
        context['pathname'] = TapLink.objects.get(
            user=self.request.user).pathname
        return context


class ProductAddFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/products.html'
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = TapLink.objects.get(user=self.request.user)
        product.save()
        for image in self.request.FILES.getlist('images'):
            ProductImage.objects.create(
                image=image,
                product=product)
        product.collections.set(list(Collection.objects.filter(name__in=form.data['collections'].split(','))))
        return redirect('products')


def add_collection_with_ajax(request):
    if request.method == 'POST':
        collection = Collection()
        collection.name = request.POST.get('collectionValue')
        collection.save()
    return render(request, 'pages/products.html')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'pages/products.html'
    success_url = reverse_lazy('products')


class BoughtProductsView(LoginRequiredMixin, ListView):
    template_name = 'pages/bought-products.html'

    def dispatch(self, request, *args, **kwargs):
        pass


class CollectionView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'pages/collection.html'
    context_object_name = 'collections'

    # def get_queryset(self):
    #     collections = Collection.objects.all().annotate(products_count=Count('name'))
    #     return collections


class ProductOwnerView(DetailView):
    model = Product
    template_name = 'pages/product-owner.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_owner'


class ShopOwnerView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'pages/shop-owner.html'
    context_object_name = 'products'

    def get_queryset(self):
        logger.success(self.kwargs)
        if self.request.GET.get('search'):
            return Product.objects.filter(
                Q(name__icontains=self.request.GET.get('search')) &
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            )
        else:
            return Product.objects.filter(
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            )


# Customer
class BuyProductView(TemplateView):
    template_name = 'pages/buy-product.html'


class CartView(TemplateView):
    template_name = 'pages/cart.html'


class ProductCustomerView(DetailView):
    model = Product
    template_name = 'pages/shop-inner.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_customer'


class ShopCustomerView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        logger.success(self.kwargs)
        if self.request.GET.get('search'):
            return Product.objects.filter(
                Q(name__icontains=self.request.GET.get('search')) &
                Q(owner__pathname=self.kwargs['pathname']) &
                Q(is_available=True)
            )
        else:
            return Product.objects.filter(
                Q(owner__pathname=self.kwargs['pathname']) &
                Q(is_available=True)
            )


class IndexCustomerView(TemplateView):
    template_name = 'pages/index-customer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taplink'] = TapLink.objects.filter(pathname=self.kwargs['pathname'])\
            .prefetch_related('messengers').prefetch_related('editors')
        return context
