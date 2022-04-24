from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "pages/index.html")
def login(request):
    return render(request, "pages/login.html")
def credits(request):
    return render(request, 'creditos/index.html')
def newCredit(request):
    return render(request, 'creditos/new.html')
def payCredit(request):
    return render(request, 'creditos/pay.html')