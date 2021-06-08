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


class ProductListView(LoginRequiredMixin, ListView):
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
    template_name = 'pages/products.html'
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save(commit=False)
        collection, _ = Collection.objects.get_or_create(
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
        return redirect('products_page')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'pages/products.html'
    success_url = reverse_lazy('products_page')


class ShopView(ListView):
    model = Product
    template_name = 'pages/shop.html'
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


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'pages/product.html'


class ProductsSoldView(TemplateView):
    template_name = 'pages/products-sold.html'


class CartView(TemplateView):
    template_name = 'pages/cart.html'













    # logger.info('some info')
    # logger.warning('some warning yellow')
    # print(self.kwargs['pathname'])
    # logger.error('some error red')
    # product = TapLink.objects.filter(user=self.request.user).first()
    # print(product)
    # logger.success('some success green')