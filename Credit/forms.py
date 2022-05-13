from tkinter import Widget
from django import forms
from .models import Loan

Compound_Choices = (
    ('', 'Select Compound'),
    ('EA', 'EA'),
    ('EM', 'EM')
)

loanPeriod_Choices = (
    ('', 'Select Loan Period'),
    ('Monthly', 'Monthly'),
    ('Weekly', 'Weekly'),
    ('Annually', 'Annually'),
    ('Daily', 'Daily')
)

termCalendar_Choices = (
    ('Years', 'Years'),
    ('Months', 'Months'),
    ('Days', 'Days')
)

class addLoanForm(forms.ModelForm):

    Compound = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=Compound_Choices)
    disbursementDate = forms.DateTimeField()
    loanPeriod = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=loanPeriod_Choices)
    loanName = forms.CharField(widget=forms.TextInput)
    termCalendar = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=termCalendar_Choices)

    class Meta:
        model = Loan
        StartDate = forms.DateField()
        fields = ('Amount', 'Term', 'StartDate', 'InterestRate')
    
    def clean(self):
        super(addLoanForm, self).clean()

        loanAmmount = self.cleaned_data.get('Amount')
        startDate = self.cleaned_data.get('StartDate')
        disbursementDate = self.cleaned_data.get('disbursementDate')
        loanTerm = self.cleaned_data.get('Term')
        interestRate = self.cleaned_data.get('InterestRate')

        if loanAmmount <= 0:
            self.add_error('Amount', 'The Loan Ammount must be higher than 0.')
        
        if startDate < disbursementDate:
            self.add_error('StartDate', 'The Start Date must be after the Disbursement Date.')
        
        if loanTerm <= 0 :
            self.add_error('Term', 'The Loan Term must be higher than 0.')
        
        if interestRate < 0 or interestRate > 100 :
            self.add_error('InterestRate', 'The Interest Rate must be between 0 and 100')
        
        return self.cleaned_data
