from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.users.forms import EditProfileForm
from apps.users.models import CustomUser


class RegistrationView(TemplateView):
    template_name = 'pages/registration.html'


class RegistrationNumberView(TemplateView):
    template_name = 'pages/registration-number.html'


def validate_phone_number(request):
    phone_number = request.GET.get('phone_number', None)
    data = {
        'is_taken': CustomUser.objects.filter(phone_number__iexact=phone_number).exists()
    }
    return JsonResponse(data)


class RegistrationSubmitView(TemplateView):
    template_name = 'pages/registration-submit.html'


class UserLoginView(LoginView):
    template_name = 'pages/sign-in.html'


class UserLogoutView(LogoutView):
    next_page = '/'


class EditProfileFormView(LoginRequiredMixin, FormView):
    form_class = EditProfileForm
    template_name = 'pages/edit-profile.html'

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save(update_fields=['first_name', 'last_name'])
        return HttpResponseRedirect(
            reverse('edit-profile', kwargs={'pk': self.request.user.pk})
        )


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'pages/change-password.html'
    success_url = reverse_lazy('change-password-done_page')


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'pages/change-password-done.html'


class ChangeNumberSubmitView(TemplateView):
    template_name = 'pages/change-number-submit.html'


class ChangeNumberView(TemplateView):
    template_name = 'pages/change-number.html'


class IndexView(TemplateView):
    template_name = 'pages/index.html'
