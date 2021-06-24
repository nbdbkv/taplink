from django.contrib import admin

from .models import TapLink, Editor, Messenger


@admin.register(TapLink)
class TapLinkAdmin(admin.ModelAdmin):
    list_display = ('pathname', 'avatar', 'user')


@admin.register(Editor)
class EditorAdmin(admin.ModelAdmin):
    list_display = ('editor',)


@admin.register(Messenger)
class MessengerAdmin(admin.ModelAdmin):
    list_display = ('telegram', 'title_t', 'whatsapp', 'title_wa')
