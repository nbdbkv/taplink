from django import forms

from .models import TapLink, Editor, Messenger


class PathNameForm(forms.ModelForm):
    class Meta:
        model = TapLink
        fields = ('pathname',)


class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = ('editor',)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = TapLink
        fields = ('avatar',)


class MessengerForm(forms.ModelForm):
    class Meta:
        model = Messenger
        fields = ('telegram', 'title_t', 'whatsapp', 'title_wa')
