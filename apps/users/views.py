from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from apps.users.forms import EditProfileForm


class RegistrationView(TemplateView):
    template_name = 'pages/registration.html'


class RegistrationNumberView(TemplateView):
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


class ChangeNumberSubmitView(TemplateView):
    template_name = 'pages/change-number-submit.html'


class ChangeNumberView(TemplateView):
    template_name = 'pages/change-number.html'


class IndexView(TemplateView):
    template_name = 'pages/index.html'
