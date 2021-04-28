from django.urls import path

from .views import (
    RegistrationView, RegistrationNumberView, ProfileUpdateView, IndexView,
    UserLoginView, UserLogoutView, UserPasswordChangeView,
    UserPasswordChangeDoneView, validate_phone_number, ChangeNumberFormView,
    UserPasswordResetFormView
)

urlpatterns = [
    path('sign-in/', UserLoginView.as_view(), name='sign-in_page'),
    path('registration/', RegistrationView.as_view(), name='reg_page'),
    path('registration-number/', RegistrationNumberView.as_view(), name='reg-number_page'),
    path('validate-number/', validate_phone_number, name='val-number_page'),
    path('edit-profile/<int:pk>/', ProfileUpdateView.as_view(), name='edit-profile'),
    path('change-password/', UserPasswordChangeView.as_view(), name='change-password_page'),
    path('change-password-done/', UserPasswordChangeDoneView.as_view(), name='change-password-done_page'),
    path('reset-password/', UserPasswordResetFormView.as_view(), name='reset-password_page'),
    path('change-number/', ChangeNumberFormView.as_view(), name='change-num_page'),
    path('log-out/', UserLogoutView.as_view(), name='log-out'),
    path('', IndexView.as_view(), name='index_page'),
]
