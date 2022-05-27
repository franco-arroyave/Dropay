from audioop import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Loan
from django.contrib import messages
from .forms import addLoanForm
from .loanInfo import LoanInfo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def loans(request):
    loansList = Loan.objects.filter(UserID_id=request.user.id)
    return render(request, 'pages/index.html', {'loans': loansList})

@login_required(login_url='login')
def newLoan(request):
    form = addLoanForm()
    return render(request, 'pages/new.html', {'form': form})

@login_required(login_url='login')
def loanPayment(request):
    return render(request, 'pages/payment.html')

@login_required(login_url='login')
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

            messages.add_message(request, messages.SUCCESS, 'Loan ' + system.get('Name') + ' added successfully!')
            return redirect('loans')

        else :
            messages.add_message(request, messages.ERROR, form.errors)
            return render(request, 'pages/loanSummary.html')
        
    else :
        form = addLoanForm()
        return render(request, 'pages/new.html', {'form': form})

@login_required(login_url='login')
def deleteLoan(request, pk):
    loan = get_object_or_404(Loan, LoanID = pk)

    if request.method == 'POST':
        loan.delete()
        messages.add_message(request, messages.SUCCESS, 'Loan deleted successfully!')
        return redirect('loans')
        
    return render(request, 'pages/index.html', {'loan' : loan})