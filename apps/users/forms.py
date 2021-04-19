from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name')


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('phone_number', 'first_name', 'last_name')
