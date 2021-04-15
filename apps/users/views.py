from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView

from apps.users.forms import EditProfileForm, RegistrationNumberForm


class RegistrationView(TemplateView):
    template_name = 'pages/registration.html'


class RegistrationNumberView(FormView):
    form_class = RegistrationNumberForm
    template_name = 'pages/registration-number.html'


class RegistrationSubmitView(TemplateView):
    template_name = 'pages/registration-submit.html'


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


class _PasswordChangeView(PasswordChangeView):
    template_name = 'pages/change-password.html'
    success_url = reverse_lazy('change-password-done_page')


class _PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'pages/change-password-done.html'


class ChangeNumberSubmitView(TemplateView):
    template_name = 'pages/change-number-submit.html'


class ChangeNumberView(TemplateView):
    template_name = 'pages/change-number.html'


class IndexView(TemplateView):
    template_name = 'pages/index.html'
