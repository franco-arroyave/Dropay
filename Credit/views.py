from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Loan
from django.contrib import messages
# Create your views here.

def loans(request):
    loansList = Loan.objects.all()
    return render(request, 'pages/index.html', {'loans': loansList})

def newLoan(request):
    return render(request, 'pages/new.html')

def loanPayment(request):
    return render(request, 'pages/payment.html')

def addLoanSummary(request):
    context = {}
    system = request.POST
    context['system'] = system
    if int(system.get('loan_ammount')) <= 0:
        messages.add_message(request, messages.ERROR, 'The Loan Ammount must be higher than 0.')
        return redirect(request.META.get('HTTP_REFERER'))
        #return HttpResponseRedirect(request.path_info)
    else :
        return render(request, 'pages/loanSummary.html', context)
