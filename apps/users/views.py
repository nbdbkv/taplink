from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, FormView

from apps.users.forms import CustomUserCreationForm, ChangeNumberForm
from apps.users.models import CustomUser


class RegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('index_page')
    template_name = 'pages/registration.html'


class RegistrationNumberView(TemplateView):
    template_name = 'pages/registration-number.html'


class ChangeNumberFormView(LoginRequiredMixin, FormView):
    form_class = ChangeNumberForm
    template_name = 'pages/change-number.html'

    def form_valid(self, form):
        user = self.request.user
        user.phone_number = form.cleaned_data['phone_number']
        user.save()
        return HttpResponseRedirect(
            reverse('edit-profile', kwargs={'pk': self.request.user.pk})
        )


def validate_phone_number(request):
    phone_number = request.GET.get('phone_number')
    data = {
        'is_taken': CustomUser.objects.filter(phone_number=phone_number).exists()
    }
    return JsonResponse(data)


class UserLoginView(LoginView):
    template_name = 'pages/sign-in.html'


class UserLogoutView(LogoutView):
    next_page = 'index_page'


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ('first_name', 'last_name')
    template_name = 'pages/edit-profile.html'


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'pages/change-password.html'
    success_url = reverse_lazy('change-password-done_page')


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'pages/change-password-done.html'


class IndexView(TemplateView):
    template_name = 'pages/index.html'
