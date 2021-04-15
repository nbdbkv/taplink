from django.urls import path

from .views import (
    RegistrationView, RegistrationNumberView, RegistrationSubmitView,
    EditProfileFormView, ChangeNumberSubmitView, ChangeNumberView,
    IndexView, _LoginView, _LogoutView, _PasswordChangeView,
    _PasswordChangeDoneView
)

urlpatterns = [
    path('sign-in/', _LoginView.as_view(), name='sign-in_page'),
    path('registration/', RegistrationView.as_view(), name='reg_page'),
    path('registration-number/', RegistrationNumberView.as_view(), name='reg-number_page'),
    path('registration-submit/', RegistrationSubmitView.as_view(), name='registration-submit_page'),
    path('edit-profile/<int:pk>/', EditProfileFormView.as_view(), name='edit-profile'),
    path('change-password/', _PasswordChangeView.as_view(), name='change-password_page'),
    path('change-password-done/', _PasswordChangeDoneView.as_view(), name='change-password-done_page'),
    path('change-number-submit/', ChangeNumberSubmitView.as_view(), name='change-num-submit_page'),
    path('change-number/', ChangeNumberView.as_view(), name='change-num_page'),
    path('log-out/', _LogoutView.as_view(), name='log-out'),
    path('', IndexView.as_view(), name='index_page'),
]
