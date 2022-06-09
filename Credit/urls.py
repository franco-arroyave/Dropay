from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('loans', views.loans, name='loans'),
    path('loans/newLoan', views.newLoan, name='newLoan'),
    path(r'^addPayment/(?P<pk>[0-9]+)/$', views.loanPayment, name='loanPayment'),
    path('loans/addLoan', views.addLoanSummary, name='loanSummary'),
    path('loans/saveLoan', views.saveLoanInfo, name='saveLoanInfo'),
    path(r'^delete/(?P<pk>[0-9]+)/$', views.deleteLoan, name='loan_delete')
]

urlpatterns += staticfiles_urlpatterns()