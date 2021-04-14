from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
)
from django.urls import path, reverse_lazy

from .views import (
    RegistrationView, RegistrationNumberView, RegistrationSubmitView,
    EditProfileFormView, ChangeNumberSubmitView, ChangeNumberView,
    IndexView
)

urlpatterns = [
    path('sign-in/',
         LoginView.as_view(template_name='pages/sign-in.html'),
         name='sign-in_page'),
    path('registration/', RegistrationView.as_view(), name='reg_page'),
    path('registration-number/',
         RegistrationNumberView.as_view(), name='reg-number_page'),
    path('registration-submit/',
         RegistrationSubmitView.as_view(), name='registration-submit_page'),
    path('edit-profile/<int:pk>/',
         EditProfileFormView.as_view(), name='edit-profile'),
    path('change-password/',
         PasswordChangeView.as_view(
             template_name='pages/change-password.html',
             success_url=reverse_lazy('change-password-done_page')),
         name='change-password_page'),
    path('change-password-done/',
         PasswordChangeDoneView.as_view(
             template_name='pages/change-password-done.html'),
         name='change-password-done_page'),
    path('change-number-submit/',
         ChangeNumberSubmitView.as_view(), name='change-num-submit_page'),
    path('change-number/', ChangeNumberView.as_view(), name='change-num_page'),
    path('log-out/', LogoutView.as_view(next_page='/'), name='log-out'),
    path('', IndexView.as_view(), name='index_page'),
]
