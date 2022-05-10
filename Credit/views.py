from django.shortcuts import render
from django.http import HttpResponse
from .models import Loan
# Create your views here.

def loans(request):
    loansList = loan.objects.all()
    return render(request, 'pages/index.html', {'loans': loansList})
def newLoan(request):
    return render(request, 'pages/new.html')
def loanPayment(request):
    return render(request, 'pages/payment.html')
