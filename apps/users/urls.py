from django.urls import path

from .views import (
    RegistrationView, RegistrationNumberView, RegistrationSubmitView,
    EditProfileFormView, ChangeNumberSubmitView, ChangeNumberView,
    IndexView, UserLoginView, UserLogoutView, UserPasswordChangeView,
    UserPasswordChangeDoneView, validate_phone_number
)

urlpatterns = [
    path('sign-in/', UserLoginView.as_view(), name='sign-in_page'),
    path('registration/', RegistrationView.as_view(), name='reg_page'),
    path('registration-number/', RegistrationNumberView.as_view(), name='reg-number_page'),
    path('validate-number/', validate_phone_number, name='val-number_page'),
    path('registration-submit/', RegistrationSubmitView.as_view(), name='registration-submit_page'),
    path('edit-profile/<int:pk>/', EditProfileFormView.as_view(), name='edit-profile'),
    path('change-password/', UserPasswordChangeView.as_view(), name='change-password_page'),
    path('change-password-done/', UserPasswordChangeDoneView.as_view(), name='change-password-done_page'),
    path('change-number-submit/', ChangeNumberSubmitView.as_view(), name='change-num-submit_page'),
    path('change-number/', ChangeNumberView.as_view(), name='change-num_page'),
    path('log-out/', UserLogoutView.as_view(), name='log-out'),
    path('', IndexView.as_view(), name='index_page'),
]
