from django.contrib import admin

from .models import TapLink, Editor, Messenger


@admin.register(TapLink)
class TapLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'pathname', 'avatar')
    ordering = ('user',)


@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ('editor',)


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    list_display = ('telegram', 'title_t', 'whatsapp', 'title_wa')
    list_display_links = ('telegram', 'whatsapp')
