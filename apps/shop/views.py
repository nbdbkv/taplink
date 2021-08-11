from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, DeleteView

from apps.customer.models import OrderItem
from apps.shop.forms import ProductForm, ProductImageForm
from apps.shop.models import Product, ProductImage, Collection
from apps.taplink.models import TapLink


class ProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'pages/shop/products.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('search'):
            return Product.objects.filter(
                Q(name__icontains=self.request.GET.get('search')) &
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            ).prefetch_related('collections')
        else:
            return Product.objects.filter(
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            ).prefetch_related('collections')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = ProductForm
        context['image_form'] = ProductImageForm
        context['collections'] = Collection.objects.filter(products__owner__user=self.request.user).distinct()
        context['pathname'] = TapLink.objects.get(user=self.request.user).pathname
        return context


class ProductAddFormView(LoginRequiredMixin, FormView):
    template_name = 'pages/shop/products.html'
    form_class = ProductForm

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = TapLink.objects.get(user=self.request.user)
        product.save()
        for image in self.request.FILES.getlist('images'):
            ProductImage.objects.create(image=image, product=product)
        product.collections.set(list(Collection.objects.filter(name__in=form.data['collections'].split(','))))
        return redirect('products')


def add_collection_with_ajax(request):
    if request.method == 'POST':
        collection = Collection()
        collection.name = request.POST.get('collectionValue')
        collection.save()
    return render(request, 'pages/shop/products.html')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'pages/shop/products.html'
    success_url = reverse_lazy('products')


class BoughtProductsView(LoginRequiredMixin, ListView):
    model = OrderItem
    template_name = 'pages/shop/bought-products.html'
    context_object_name = 'ordered_items'
    paginate_by = 8
    queryset = OrderItem.objects.select_related('order', 'product')


class CollectionView(LoginRequiredMixin, ListView):
    model = Collection
    template_name = 'pages/shop/collection.html'
    context_object_name = 'collections'

    def get_queryset(self):
        return Collection.objects.filter(products__owner__user=self.request.user)\
            .annotate(products_per_collection=Count('products'))


class ProductOwnerView(DetailView):
    model = Product
    template_name = 'pages/shop/product-owner.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_owner'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ProductImage.objects.filter(product=self.object)
        return context


class ShopOwnerView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'pages/shop/shop-owner.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.request.GET.get('search'):
            return Product.objects.filter(
                Q(name__icontains=self.request.GET.get('search')) &
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            ).prefetch_related('images').select_related('owner')
        else:
            return Product.objects.filter(
                Q(owner__user=self.request.user) &
                Q(is_available=True)
            ).prefetch_related('images').select_related('owner')
