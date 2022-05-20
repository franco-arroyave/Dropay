import datetime
import numpy_financial as npf

class LoanInfo :

    def __init__(self, system):
        self.Term = int(system.get('Term'))
        self.termCalendar = system.get('termCalendar')
        self.Compound = system.get('Compound')
        self.InterestRate = float(system.get('InterestRate'))
        self.Ammount = float(system.get('Ammount'))
        self.StartDate = datetime.datetime.strptime(system.get('StartDate'), '%Y-%m-%d')
        self.loanPeriod = 1

    def loanSummary(self):
        loanContext = dict()
        loanContext['monthsTerm'] = LoanInfo.monthsTerm(self)
        loanContext['interestEA'] = "%.2f" % LoanInfo.convertInterestRate(self, 12)
        loanContext['monthlyPayment'] = "%.2f" % LoanInfo.monthlyPayment(self)
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

    def convertInterestRate(self, nPeriod):
        if self.Compound == "EM" :
            if nPeriod == 1 :
                return 100*(pow(1+self.InterestRate/100, 12)-1)
            else :
                return 100*(pow(1+self.InterestRate/100, 12/nPeriod)-1)
        else:
            if nPeriod == 12 :
                return self.InterestRate
            else :
                return 100*(pow(1+self.InterestRate/100, nPeriod/12)-1)
    
    def monthlyPayment(self):
        return -1*npf.pmt(LoanInfo.convertInterestRate(self, 12)/100, LoanInfo.monthsTerm(self), self.Ammount)

    def loanChart(self):
        chartInfo = dict()
        chartInfo['categories'] = LoanInfo.chartCategories(self)
        chartInfo['interest'] = LoanInfo.chartInterest(self)
        chartInfo['principal'] = LoanInfo.chartPrincipal(self)
        chartInfo['balance'] = LoanInfo.chartBalance(self)
        return chartInfo

    def chartCategories(self) :
        months = LoanInfo.monthsTerm(self)
        strCategories = ''
        for i in range(months) :
            newDate = (self.StartDate + datetime.timedelta(i * 30)).date().strftime('%d/%m/%Y')
            strCategories +=  '\'' + str(newDate) + '\', '
        return strCategories
    
    def chartInterest(self) :
        months = LoanInfo.monthsTerm(self)
        mpt = LoanInfo.monthlyPayment(self)
        balance = self.Ammount
        interest = 0
        principal = 0
        strInterest = ''
        interestRate = pow(1+LoanInfo.convertInterestRate(self, 12)/100, 1/12)-1
        for i in range(months) :
            interest = interestRate*balance
            principal = mpt - interest
            balance = balance - principal
            strInterest += str("%.2f" % interest) + ', '
        return strInterest

    def chartPrincipal(self) :
        months = LoanInfo.monthsTerm(self)
        mpt = LoanInfo.monthlyPayment(self)
        balance = self.Ammount
        interest = 0
        principal = 0
        strPrincipal = ''
        interestRate = pow(1+LoanInfo.convertInterestRate(self, 12)/100, 1/12)-1
        for i in range(months) :
            interest = interestRate*balance
            principal = mpt - interest
            balance = balance - principal
            strPrincipal += str("%.2f" % principal) + ', '
        return strPrincipal

    def chartBalance(self) :
        months = LoanInfo.monthsTerm(self)
        mpt = LoanInfo.monthlyPayment(self)
        balance = self.Ammount
        interest = 0
        principal = 0
        strBalance = ''
        interestRate = pow(1+LoanInfo.convertInterestRate(self, 12)/100, 1/12)-1
        for i in range(months) :
            interest = interestRate*balance
            principal = mpt - interest
            balance = balance - principal
            strBalance += str("%.2f" % balance) + ', '
        return strBalance