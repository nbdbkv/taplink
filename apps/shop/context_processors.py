from apps.taplink.models import TapLink


def get_pathname(request):
    pathname_context = TapLink.objects.get(user=request.user).pathname
    return dict(pathname_context=pathname_context)
