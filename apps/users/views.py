from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from apps.users.forms import ProfileEditForm #ChangePasswordForm
from apps.users.models import CustomUser


class RegistrationView(TemplateView):
    template_name = 'pages/registration.html'


class RegistrationNumberView(TemplateView):
    template_name = 'pages/registration-number.html'


class RegistrationSubmitView(TemplateView):
    template_name = 'pages/registration-submit.html'


class ProfileEditFormView(LoginRequiredMixin, FormView):
    form_class = ProfileEditForm
    template_name = 'pages/edit-profile.html'

    def form_valid(self, form):
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save(update_fields=['first_name', 'last_name'])
        return HttpResponseRedirect(
            reverse('edit-profile', kwargs={'pk': self.request.user.pk})
        )


# class PasswordChangeFormView(PasswordChangeView):
#     form_class = ChangePasswordForm
#     template_name = 'pages/change-password.html'

#     def get_form_kwargs(self):
#         print('A' * 100)
#         kwargs = super(_PasswordChangeView, self).get_form_kwargs()
#         print(kwargs)
#         print('B' * 100)
#         kwargs['user'] = CustomUser.objects.get(id=self.request.user.id)
#         return kwargs
#
#     # def get_form_kwargs(self):
#     #     kwargs = super(PasswordChangeFormView, self).get_form_kwargs()
#     #     kwargs['user'] = self.request.user
#     #     if self.request.method == 'POST':
#     #         kwargs['data'] = self.request.POST
#     #     return kwargs
#     #
#     # def form_valid(self, form):
#     #     form.save()
#     #     update_session_auth_hash(self.request, form.user)
#     #     return super(ChangePasswordFormView, self).form_valid(form)


class ChangePasswordView(TemplateView):
    template_name = 'pages/change-password.html'


# class PasswordChangeView(PasswordContextMixin, FormView):
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy('password_change_done')
#     template_name = 'registration/password_change_form.html'
#     title = _('Password change')
#
#     @method_decorator(sensitive_post_parameters())
#     @method_decorator(csrf_protect)
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs
#
#     def form_valid(self, form):
#         form.save()
#         # Updating the password logs out all other sessions for the user
#         # except the current one.
#         update_session_auth_hash(self.request, form.user)
#         return super().form_valid(form)
#

class ChangeNumberSubmitView(TemplateView):
    template_name = 'pages/change-number-submit.html'


class ChangeNumberView(TemplateView):
    template_name = 'pages/change-number.html'


class IndexView(TemplateView):
    template_name = 'pages/index.html'


# class ValidateRegistrationNumberView():
#     pass