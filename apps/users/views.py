from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, FormView

from apps.users.forms import (
    CustomUserCreationForm, ChangeNumberForm, CustomSetPasswordForm
)
from apps.users.models import CustomUser


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('sign-in_page')
    template_name = 'pages/registration.html'


class RegistrationNumberView(TemplateView):
    template_name = 'pages/registration-number.html'


class ChangeNumberFormView(LoginRequiredMixin, FormView):
    form_class = ChangeNumberForm
    template_name = 'pages/change-number.html'
    login_url = 'sign-in_page'

    def form_valid(self, form):
        user = self.request.user
        user.phone_number = form.cleaned_data['phone_number']
        user.save(update_fields=['phone_number'])
        return HttpResponseRedirect(
            reverse('edit-profile', kwargs={'pk': user.pk})
        )


def validate_phone_number(request):
    phone_number = request.GET.get('phone_number', None)
    data = {
        'is_taken': CustomUser.objects.filter(phone_number__iexact=phone_number).exists()
    }
    return JsonResponse(data)


class UserLoginView(LoginView):
    template_name = 'pages/sign-in.html'


class UserLogoutView(LogoutView):
    next_page = 'sign-in_page'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name')
    template_name = 'pages/edit-profile.html'
    login_url = 'sign-in_page'


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'pages/change-password.html'
    success_url = reverse_lazy('change-password-done_page')
    login_url = 'sign-in_page'


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'pages/change-password-done.html'
    login_url = 'sign-in_page'


class UserPasswordResetFormView(FormView):
    form_class = CustomSetPasswordForm
    template_name = 'pages/reset-password.html'

    def form_valid(self, form):
        back_number = form.cleaned_data['front_number']
        try:
            user = CustomUser.objects.get(phone_number=back_number)
        except CustomUser.DoesNotExist as err:
            raise ValidationError(
                _('Пользователь с таким номером не существует'), err)
        user.set_password(form.cleaned_data['new_password1'])
        user.save(update_fields=['password'])
        return HttpResponseRedirect(reverse('sign-in_page'))
