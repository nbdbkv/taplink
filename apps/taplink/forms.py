from django import forms

from .models import TapLink, TapLinkEditor, TapLinkMessenger


class TapLinkNickNameForm(forms.ModelForm):
    class Meta:
        model = TapLink
        fields = ('nickname',)


class TapLinkEditorForm(forms.ModelForm):
    class Meta:
        model = TapLinkEditor
        fields = ('editor',)


class TapLinkAvatarForm(forms.ModelForm):
    class Meta:
        model = TapLink
        fields = ('avatar',)


class TapLinkMessengerForm(forms.ModelForm):
    class Meta:
        model = TapLinkMessenger
        fields = ('telegram', 'title_t', 'whatsapp', 'title_wa')
