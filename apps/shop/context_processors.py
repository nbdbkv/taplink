from apps.customer.cart import Cart
from apps.taplink.models import TapLink


def pathname(request):
    pathname_context = None
    if request.user.is_authenticated:
        pathname_context = TapLink.objects.get(user=request.user).pathname
    return dict(pathname_context=pathname_context)


def cart(request):
    return {'cart': Cart(request)}
