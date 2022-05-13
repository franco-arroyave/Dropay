from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from . import views

urlpatterns = [
    path('', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('accounts/login/', LoginView.as_view(template_name='pages/login.html')),
    path('logout', LogoutView.as_view(template_name='pages/login.html'), name='logout'),
    path('signup', views.signUp, name='signup'),
    path('home', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()