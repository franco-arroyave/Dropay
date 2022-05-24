from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Ususario {username} creado exitosamente')
            return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
            # messages.success(request, f'Error al diligenciar el formulario')
    else:
        form = UserRegisterForm()
        # messages.success(request, f'Hello register')
    context = {'form' : form}
    return render(request, 'pages/signUp.html', context)




    #def insert_init_documentType(apps, schema_editor):
    #    typeID = apps.get_model('User', 'TypeID')
    #    types = ['Cédula', 'Cédula Extrangeria','NIT', 'Tarjeta de Identidad']
    #    for i in types:
    #        typeID.objects.create(Description = i)

    #def undo_insert_documentType(apps, schema_editor):
    #    typeID = apps.get_model('User', 'TypeID')
    #    typeID.objects.all().delete()

#     migrations.RunPython(insert_init_documentType, reverse_code=undo_insert_documentType)