from django.contrib import admin

from .models import TapLink, TapLinkEditor, TapLinkMessenger


@admin.register(TapLink)
class TapLinkAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'avatar', 'user')


@admin.register(TapLinkEditor)
class TapLinkEditorAdmin(admin.ModelAdmin):
    list_display = ('editor',)


@admin.register(TapLinkMessenger)
class TapLinkMessengerAdmin(admin.ModelAdmin):
    list_display = ('telegram', 'title_t', 'whatsapp', 'title_wa')
