from audioop import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Loan, Paymant
from django.contrib import messages
from .forms import addLoanForm, addRegularPayment
from .loanInfo import LoanInfo
from django.contrib.auth.decorators import login_required
from django.db.models import Subquery, OuterRef
# Create your views here.

@login_required(login_url='login')
def loans(request):
    loansList = Loan.objects.filter(UserID_id=request.user.id).annotate(balance = Subquery(Paymant.objects.filter(LoanID_id=OuterRef('pk')).order_by('-Date').values('Balance')[:1])).order_by('-StartDate')
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
            # saveLoan.save()

            context = {}
            system = request.POST
            context['system'] = system
            context['loanInfo'] = LoanInfo(system).loanSummary()
            context['loanChart'] = LoanInfo(system).loanChart()
            context['loanSchedule'] = LoanInfo(system).loanSchedule()
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
        formLoan = addLoanForm(system)
        if formLoan.is_valid() :
            saveLoan = formLoan.save(commit=False)
            saveLoan.UserID_id = request.user.id
            saveLoan.Periodicity_id = system.get('loanPeriod')
            saveLoan.monthlyPayment = system.get('monthlyPayment')
            saveLoan.save()
            loanPK = saveLoan.pk

            lstRegularPayments = LoanInfo(system).addRegularPayments(loanPK, int(system.get('Payments')))
            for regularPayment in lstRegularPayments:
                formPayments = addRegularPayment(regularPayment)
                if formPayments.is_valid():
                    savePayment = formPayments.save(commit=False)
                    savePayment.save()
                else :
                    messages.add_message(request, messages.ERROR, formPayments.errors)
                    print(formPayments.errors)

            messages.add_message(request, messages.SUCCESS, 'Loan ' + system.get('Name') + ' added successfully!')
            return redirect('loans')

        else :
            messages.add_message(request, messages.ERROR, formLoan.errors)
            return render(request, 'pages/loanSummary.html')
        
    else :
        formLoan = addLoanForm()
        return render(request, 'pages/new.html', {'form': formLoan})

@login_required(login_url='login')
def deleteLoan(request, pk):
    loan = get_object_or_404(Loan, LoanID = pk)

    if request.method == 'POST':
        loan.delete()
        messages.add_message(request, messages.SUCCESS, 'Loan deleted successfully!')
        return redirect('loans')
        
    return render(request, 'pages/index.html', {'loan' : loan})