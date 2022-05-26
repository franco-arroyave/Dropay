from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, ProfileRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import  method_decorator
from django.contrib.auth import login

# Create your views here.
@login_required(login_url='login')
#@method_decorator(login_required, name='login')
def index(request):
    return render(request, "pages/index.html")

def signUp(request):
    if request.method == "POST":
        userForm = UserRegisterForm(request.POST)
        profileForm = ProfileRegisterForm(request.POST)
        if userForm.is_valid() and profileForm.is_valid:
            user = userForm.save(commit = False)
            user.save()
            profile = profileForm.save(commit = False)
            
            profile.user = user
            profile.save()
            username = userForm.cleaned_data['username']
            messages.success(request, f'Ususario {username} creado exitosamente')
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, userForm.errors)
            messages.add_message(request, messages.ERROR, profileForm.errors)
    else:
        userForm = UserRegisterForm()
        profileForm = ProfileRegisterForm()
    context = {'userForm' : userForm, 'profileForm' : profileForm}
    return render(request, 'pages/signUp.html', context)
