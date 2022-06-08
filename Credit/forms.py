from dataclasses import fields
from email.policy import default
from random import choices
from tkinter import Widget
from django import forms
from .models import Loan, Paymant, Periodicity

Compound_Choices = (
    ('', 'Select Compound'),
    ('EA', 'EA'),
    ('EM', 'EM')
)

termCalendar_Choices = (
    ('Years', 'Years'),
    ('Months', 'Months'),
    ('Days', 'Days')
)

class addLoanForm(forms.ModelForm):

    Compound = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=Compound_Choices)
    loanPeriod = forms.ModelChoiceField(widget=forms.Select(attrs={"class": "form-select"}), queryset=Periodicity.objects.all(), empty_label="Select Period")
    # loanName = forms.CharField(widget=forms.TextInput)
    termCalendar = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=termCalendar_Choices)

    class Meta:
        model = Loan
        # StartDate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        fields = ('Name','Ammount', 'Term', 'StartDate', 'DisbursementDate', 'InterestRate')
        widgets = {
            'StartDate' : forms.widgets.DateInput(attrs={'type': 'text', 
                                                        'onfocus' : "(this.type='date')",
                                                        'onblur' : "if(!this.value) this.type='text'"}),
            'DisbursementDate' : forms.widgets.DateInput(attrs={'type': 'text', 
                                                        'onfocus' : "(this.type='date')",
                                                        'onblur' : "if(!this.value) this.type='text'"}),
            'Name' : forms.widgets.TextInput(attrs={'type' : 'text'})
        }
    
    def clean(self):
        super(addLoanForm, self).clean()

        loanAmmount = self.cleaned_data.get('Ammount')
        startDate = self.cleaned_data.get('StartDate')
        DisbursementDate = self.cleaned_data.get('DisbursementDate')
        loanTerm = self.cleaned_data.get('Term')
        interestRate = self.cleaned_data.get('InterestRate')

        if loanAmmount <= 0:
            self.add_error('Ammount', 'The Loan Ammount must be higher than 0.')
        
        if startDate < DisbursementDate:
            self.add_error('StartDate', 'The Start Date must be after the Disbursement Date.')
        
        if loanTerm <= 0 :
            self.add_error('Term', 'The Loan Term must be higher than 0.')
        
        if interestRate < 0 :
            self.add_error('InterestRate', 'The Interest Rate must be higher than 0.')
        
        return self.cleaned_data

class addRegularPayment(forms.ModelForm) :

    class Meta :
        model = Paymant
        fields = ('Date', 'Payment', 'Pricipal', 'Interest', 'Balance', 'LoanID')


