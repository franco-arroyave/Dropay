from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "pages/index.html")
def loans(request):
    return render(request, 'loans/index.html')
def newLoan(request):
    return render(request, 'loans/new.html')
def loanPayment(request):
    return render(request, 'loans/payment.html')
def logIn(request):
    return render(request, 'pages/logIn.html')
def signUp(request):
    return render(request, 'pages/signUp.html')