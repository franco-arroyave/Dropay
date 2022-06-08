from hashlib import algorithms_available
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, ProfileRegisterForm, updateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'pages/index.html')

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
            messages.success(request, f'User {username} created successfully')
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, userForm.errors)
            messages.add_message(request, messages.ERROR, profileForm.errors)
    else:
        userForm = UserRegisterForm()
        profileForm = ProfileRegisterForm()
    context = {'userForm' : userForm, 'profileForm' : profileForm}
    return render(request, 'pages/signUp.html', context)

@login_required(login_url='login')
def updateUser(request):
    if request.method == "POST":
        userForm = updateUserForm(request.POST, instance= request.user)
        if userForm.is_valid():
            userForm.save()
            messages.success(request, f'User updated successfully')
            return render(request, 'pages/index.html')
        else:
            messages.add_message(request, messages.ERROR, userForm.errors)
    else:
        userForm = updateUserForm(instance=request.user)
    context = {'userForm': userForm}
    return render(request, 'pages/update.html', context)


