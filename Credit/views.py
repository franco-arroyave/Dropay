from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Loan
from django.contrib import messages
from .forms import addLoanForm
from .loanInfo import LoanInfo
# Create your views here.

def loans(request):
    loansList = Loan.objects.all()
    return render(request, 'pages/index.html', {'loans': loansList})

def newLoan(request):
    form = addLoanForm()
    return render(request, 'pages/new.html', {'form': form})

def loanPayment(request):
    return render(request, 'pages/payment.html')

def addLoanSummary(request):

    if request.method == "POST":
        form = addLoanForm(request.POST)
        if form.is_valid() :
            saveLoan = form.save(commit=False)
            saveLoan.UserID_id = request.user.id
            saveLoan.Periodicity_id = 1
            # saveLoan.save()

            context = {}
            system = request.POST
            context['system'] = system
            context['loanInfo'] = LoanInfo(system).loanSummary()
            context['loanChart'] = LoanInfo(system).loanChart()
            return render(request, 'pages/loanSummary.html', context)
        else :
            messages.add_message(request, messages.ERROR, form.errors)
            return render(request, 'pages/new.html', {'form': form})
    else :
        form = addLoanForm()
        return render(request, 'pages/new.html', {'form': form})

def saveLoanInfo(request):
    if request.method == "POST":

        system = request.POST
        form = addLoanForm(system)

        if form.is_valid() :
            saveLoan = form.save(commit=False)
            saveLoan.UserID_id = request.user.id
            saveLoan.Periodicity_id = system.get('loanPeriod')
            saveLoan.monthlyPayment = system.get('monthlyPayment')
            saveLoan.save()

            messages.add_message(request, messages.SUCCESS, 'Loan ' + system.get('Name') + ' added succesfully!')
            return redirect('loans')

        else :
            messages.add_message(request, messages.ERROR, form.errors)
            return render(request, 'pages/loanSummary.html')
        
    else :
        form = addLoanForm()
        return render(request, 'pages/new.html', {'form': form})
