from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from Credit import views as viewsCredit

urlpatterns = [
    path('', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='pages/login.html')),
    path('logout', LogoutView.as_view(template_name='pages/login.html'), name='logout'),
    path('signup', views.signUp, name='signup'),
    path('home', viewsCredit.loans, name='index'),
    path('updateUser', views.updateUser, name='updateUser'),
    path('updatePassword', PasswordChangeView.as_view(template_name='pages/updatePassword.html'), name='updatePassword'),
    path('resetPassword', PasswordResetView.as_view(template_name='passwordReset/pass_reset_form.html'), name='resetPassword'),
    path('resetPassword/done', PasswordResetDoneView.as_view(template_name='passwordReset/pass_reset_done.html'), name='password_reset_done'),
    path('resetPassword/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='passwordReset/pass_reset_confirm.html'), name='password_reset_confirm'),
    path('resetPassword/complete', PasswordResetCompleteView.as_view(template_name='passwordReset/pass_reset_complete.html'), name='password_reset_complete'),
]

urlpatterns += staticfiles_urlpatterns()