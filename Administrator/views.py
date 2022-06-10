from django.shortcuts import render
from django.contrib.auth.models import User
from Credit.models import Loan

# Create your views here.

def statistics(request):
    usersN = User.objects.count()
    loansN = Loan.objects.count()
    context = {'usersN': usersN, 'loansN': loansN}
    return render(request, 'pages/statistics.html', context)


