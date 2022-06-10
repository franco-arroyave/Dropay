from audioop import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Loan, Paymant
from django.contrib import messages
from .forms import addLoanForm, addRegularPayment
from .loanInfo import LoanInfo
from .payments import PaymentsInfo
from django.contrib.auth.decorators import login_required
from django.db.models import Subquery, OuterRef, Sum
# Create your views here.

@login_required(login_url='login')
def loans(request):
    loansList = Loan.objects.filter(UserID_id=request.user.id).annotate(balance = Subquery(Paymant.objects.filter(LoanID_id=OuterRef('pk')).order_by('-Date').values('Balance')[:1])).order_by('-StartDate')
    for loan in loansList:
        if loan.balance == None:
            loan.balance = loan.Ammount
    return render(request, 'pages/index.html', {'loans': loansList})

@login_required(login_url='login')
def newLoan(request):
    form = addLoanForm()
    return render(request, 'pages/new.html', {'form': form})

@login_required(login_url='login')
def addLoanSummary(request):

    if request.method == "POST":
        form = addLoanForm(request.POST)
        if form.is_valid() :
            saveLoan = form.save(commit=False)
            saveLoan.UserID_id = request.user.id
            # saveLoan.save()

            context = {}
            request.POST._mutable = True
            system = request.POST
            context['system'] = system
            context['system']['Name'] = system.get('Name').capitalize()
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

@login_required(login_url='login')
def loanPayment(request, pk):
    loan = get_object_or_404(Loan, LoanID = pk)

    if request.method == 'POST':
        loanInfo = Loan.objects.filter(LoanID=pk, UserID_id=request.user.id).annotate(balance = Subquery(Paymant.objects.filter(LoanID_id=OuterRef('pk')).order_by('-Date').values('Balance')[:1]))[0]

        if loanInfo.balance == None:
            loanInfo.balance = loanInfo.Ammount

        payments = Paymant.objects.filter(LoanID_id=pk).order_by('-Date')
        paymentSummary = PaymentsInfo(payments).paymentSummary()
        paymentsMade = PaymentsInfo(payments).paymentsMade(vars(loanInfo))
        loanSchedule = LoanInfo(PaymentsInfo(payments).loanContext(vars(loanInfo))).loanSchedule()
        loanChart = LoanInfo(PaymentsInfo(payments).loanContext(vars(loanInfo))).loanChart()
        return render(request, 'pages/payment.html', {'loan': loanInfo, 'payments': paymentsMade, 'loanSchedule': loanSchedule, 'loanChart': loanChart, 'paymentSummary': paymentSummary})
    else :
        messages.add_message(request, messages.ERROR, loanInfo.errors)
        return render(request, 'pages/index.html')


def saveLoanPayment(request):
    if request.method == "POST":
        system = request.POST
        loanID = system.get('loanID')
        numPayments = int(system.get('payments'))

        payments = Paymant.objects.filter(LoanID_id=loanID).order_by('-Date')
        lstPayments = list(payments)
        loanInfo = Loan.objects.filter(LoanID=loanID, UserID_id=request.user.id)[0]
        loanContext = PaymentsInfo(payments).loanContext(vars(loanInfo))
        lstRegularPayments = LoanInfo(loanContext).addRegularPayments(loanID, numPayments)

        changes = list()
        numChanges = 0
        if len(lstRegularPayments) > len(payments):
            numChanges = len(lstRegularPayments) - len(payments)
            changes = lstRegularPayments[len(payments):]
            print('Nuevos pagos')

            for pay in changes:
                formPayments = addRegularPayment(pay)
                if formPayments.is_valid():
                        savePayment = formPayments.save(commit=False)
                        savePayment.save()
                else :
                    messages.add_message(request, messages.ERROR, formPayments.errors)
            
            messages.add_message(request, messages.SUCCESS, 'Payment added successfully!')

        elif len(lstRegularPayments) < len(payments) :
            numChanges = len(payments) - len(lstRegularPayments)
            changes = lstPayments[:numChanges]

            for pay in changes:
                payment = get_object_or_404(Paymant, Date=pay.Date, LoanID_id=loanID)
                payment.delete()
            
            messages.add_message(request, messages.SUCCESS, 'Payment deleted successfully!')

    return loanPayment(request, loanID)

