from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('phone_number', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')


class ChangeNumberForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('phone_number',)


class CustomSetPasswordForm(forms.Form):
    front_number = forms.CharField()

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput,
    )

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
