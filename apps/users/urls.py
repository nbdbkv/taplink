from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import (
    RegistrationView, RegistrationNumberView, # PasswordChangeFormView,
    RegistrationSubmitView, ProfileEditFormView, ChangeNumberSubmitView,
    ChangeNumberView, IndexView, ChangePasswordView
)

urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='pages/sign-in.html'), name='sign-in_page'),
    path('registration/', RegistrationView.as_view(), name='reg_page'),
    path('registration-number/', RegistrationNumberView.as_view(), name='reg-number_page'),
    # path('registration-number/validate', ValidateRegistrationNumberView.as_view(), name='reg-number_page'),
    path('registration-submit/', RegistrationSubmitView.as_view(), name='registration-submit_page'),
    path('edit-profile/<int:pk>/', ProfileEditFormView.as_view(), name='edit-profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password_page'),
    # path('change-password/', PasswordChangeFormView.as_view(), name='change-password_page'),
    path('change-number-submit/', ChangeNumberSubmitView.as_view(), name='change-num-submit_page'),
    path('change-number/', ChangeNumberView.as_view(), name='change-num_page'),
    path('log-out/', LogoutView.as_view(next_page='/'), name='log-out'),
    path('', IndexView.as_view(), name='index_page'),
]
