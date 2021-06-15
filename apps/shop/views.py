from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, FormView, ListView, DetailView, DeleteView
)
from loguru import logger

from apps.shop.forms import CollectionForm, ProductForm, ProductImageForm
from apps.shop.models import Product, ProductImage, Collection
from apps.taplink.models import TapLink


class ProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'pages/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Product.objects.filter(
                Q(seller=self.request.user) &
                Q(product_name__icontains=query)
            )
        else:
            return Product.objects.filter(seller=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collection_form'] = CollectionForm
        context['product_form'] = ProductForm
        context['image_form'] = ProductImageForm
        context['pathname'] = TapLink.objects.get(user=self.request.user).pathname
        return context


class ProductAddFormView(LoginRequiredMixin, FormView):
    form_class = ProductForm
    template_name = 'pages/products.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        collection, is_created = Collection.objects.get_or_create(
            collection_name=self.request.POST.get('collection_name')
        )
        product.collection = collection
        product.seller = self.request.user
        product.save()
        images = self.request.FILES.getlist('image')
        for image in images:
            ProductImage.objects.create(
                image=image,
                product=product)
        return redirect('products')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'pages/products.html'
    success_url = reverse_lazy('products')


# class ShopView(ListView):
#     model = Product
#     template_name = 'pages/shop.html'
#     context_object_name = 'products'
#
#     def get_queryset(self):
#         query = self.request.GET.get('search')
#         print(self.request.GET)
#         if query:
#             return Product.objects.filter(
#                 # Q(seller=self.request.user) &
#                 Q(product_name__icontains=query)
#             )
#         else:
#             return Product.objects.filter(is_available=True)


class ProductCollectionListView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'pages/shop.html'
    # context_object_name = ''

    def get_queryset(self):
        return Collection.objects.filter(slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('A' * 70, context)
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductImage.objects.filter(
            product__slug=self.kwargs['slug']
        )
        return context


class ProductsSoldView(TemplateView):
    template_name = 'pages/products-sold.html'


# class CartView(TemplateView):
#     template_name = 'pages/cart.html'


class ShopView(ListView):
    model = Product
    template_name = 'pages/shop.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        print(self.request.GET)
        if query:
            return Product.objects.filter(
                # Q(seller=self.request.user) &
                Q(product_name__icontains=query)
            )
        else:
            return Product.objects.filter(is_available=True)


class ShopOwnerView(TemplateView):
    template_name = 'pages/shop-owner.html'


class ShopInnerView(TemplateView):
    template_name = 'pages/shop-inner.html'


class CartView(TemplateView):
    template_name = 'pages/cart.html'


class BoughtProductsView(TemplateView):
    template_name = 'pages/bought-products.html'


class CollectionView(TemplateView):
    template_name = 'pages/collection.html'


class BuyProductView(TemplateView):
    template_name = 'pages/buy-product.html'
