from django.urls import path

from apps.taplink.views import (
    IndexView, PathNameFormView, EditorFormView,
    AvatarFormView, MessengerFormView,
)

urlpatterns = [
    path('pathname/', PathNameFormView.as_view(), name='pathname_page'),
    path('editor/', EditorFormView.as_view(), name='editor_page'),
    path('avatar/', AvatarFormView.as_view(), name='avatar_page'),
    path('messenger/', MessengerFormView.as_view(), name='messenger_page'),
    path('', IndexView.as_view(), name='index_page'),
]
