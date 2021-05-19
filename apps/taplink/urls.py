from django.urls import path

from apps.taplink.views import (
    IndexView, TapLinkNickNameFormView, TapLinkEditorFormView,
    TapLinkAvatarFormView, TapLinkMessengerFormView,
)

urlpatterns = [
    path('nickname/', TapLinkNickNameFormView.as_view(), name='nickname_page'),
    path('editor/', TapLinkEditorFormView.as_view(), name='editor_page'),
    path('avatar/', TapLinkAvatarFormView.as_view(), name='avatar_page'),
    path('messenger/', TapLinkMessengerFormView.as_view(), name='messenger_page'),
    path('', IndexView.as_view(), name='index_page'),
]
