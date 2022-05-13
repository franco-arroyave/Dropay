import numpy_financial as npf

class LoanInfo :

    def __init__(self, system):
        self.Term = int(system.get('Term'))
        self.termCalendar = system.get('termCalendar')
        self.Compound = system.get('Compound')
        self.InterestRate = float(system.get('InterestRate'))
        self.Ammount = float(system.get('Amount'))

    def loanSummary(self):
        loanContext = dict()
        loanContext['monthsTerm'] = LoanInfo.monthsTerm(self)
        loanContext['interestEA'] = LoanInfo.convertInterestRate(self)
        loanContext['monthlyPayment'] = LoanInfo.monthlyPayment(self)
        return loanContext

    def monthsTerm(self):
        months = 0
        if self.termCalendar == "Years":
            months = self.Term * 12
        elif self.termCalendar == "Days":
            months = self.Term / 30
        else :
            months = self.Term
        return months

    def convertInterestRate(self):
        if self.Compound == "EM" :
            return 100*(pow(1+self.InterestRate/100, 12)-1)
        else:
            return self.InterestRate
    
    def monthlyPayment(self):
        return -1*npf.pmt(self.InterestRate/100, LoanInfo.monthsTerm(self), self.Ammount)