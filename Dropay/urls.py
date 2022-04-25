from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.logIn, name='login'),
    path('login', views.logIn, name='login'),
    path('home', views.index, name='index'),
    path('loans', views.loans, name='loans'),
    path('loans/newLoan', views.newLoan, name='newLoan'),
    path('loans/addPayment', views.loanPayment, name='loanPayment'),
]

urlpatterns += staticfiles_urlpatterns()