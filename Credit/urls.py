from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('loans', views.loans, name='loans'),
    path('loans/newLoan', views.newLoan, name='newLoan'),
    path('loans/addPayment', views.loanPayment, name='loanPayment'),
]

urlpatterns += staticfiles_urlpatterns()