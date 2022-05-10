from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.logIn, name='login'),
    path('login', views.logIn, name='login'),
    path('signup', views.signUp, name='signup'),
    path('home', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()