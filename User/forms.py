from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import xUser 
from .models import TypeID

class UserRegisterForm(UserCreationForm):
    
    document = forms.CharField(label='Document', widget=forms.TextInput)
    documentType = forms.ModelChoiceField(empty_label='Document Type',queryset=TypeID.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    birthday = forms.CharField(label='Birthday', widget=forms.TextInput)
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
    last_name = forms.CharField(required=True)

    class Meta:
        model = xUser
        fields = ['document', 
        'documentType', 
        'first_name', 
        'last_name', 
        'email', 
        'username', 
        'password1', 
        'password2', 
        'birthday']

        help_texts = {k:"" for k in fields}
