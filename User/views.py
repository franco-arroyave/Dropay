from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "pages/index.html")
def logIn(request):
    return render(request, 'pages/logIn.html')
def signUp(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Ususario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()
        messages.success(request, f'Hello register')
        print('hello register')
    context = {'from' : form}
    return render(request, 'pages/signUp.html', context)