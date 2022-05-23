import datetime
from dateutil.relativedelta import relativedelta
import numpy_financial as npf

class LoanInfo :

    def __init__(self, system):
        self.Term = int(system.get('Term'))
        self.termCalendar = system.get('termCalendar')
        self.Compound = system.get('Compound')
        self.InterestRate = float(system.get('InterestRate'))
        self.Ammount = float(system.get('Ammount'))
        self.StartDate = datetime.datetime.strptime(system.get('StartDate'), '%Y-%m-%d')
        self.loanPeriod = int(system.get('loanPeriod'))
        self.gralPeriod = 1

    def loanSummary(self):
        loanContext = dict()
        loanContext['monthsTerm'] = LoanInfo.monthsTerm(self)
        self.gralPeriod = 1
        loanContext['interestEA'] = "%.2f" % LoanInfo.convertInterestRate(self, 1)
        loanContext['monthlyPayment'] = "%.2f" % LoanInfo.monthlyPayment(self)
        return loanContext

    def monthsTerm(self):
        self.gralPeriod = 12
        months = 0
        if self.termCalendar == "Years":
            months = self.Term * 12
        elif self.termCalendar == "Days":
            months = self.Term / 30
        else :
            months = self.Term
        return months
    
    def weeksTerm(self) :
        self.gralPeriod = 52
        weeks = 0
        if self.termCalendar == "Years":
            weeks = self.Term * 52
        elif self.termCalendar == "Days":
            weeks = self.Term / 7
        else :
            weeks = self.Term * 4
        return weeks
    
    def daysTerm(self) :
        self.gralPeriod = 365
        days = 0
        if self.termCalendar == "Years":
            days = self.Term * 365
        elif self.termCalendar == "Days":
            days = self.Term
        else :
            days = self.Term * 30
        return days

    def convertInterestRate(self, Period):
        if self.Compound == "EM" :
            return 100*(pow(1+self.InterestRate/100, 12/self.gralPeriod)-1)
        else:
            return 100 * (pow(1+self.InterestRate/100, 1/self.gralPeriod)-1)
    
    def convertPeriod(self) :
        if self.loanPeriod == 1 : #Annually
            return 1 * self.Term
        elif self.loanPeriod == 2 : #Monthly
            term = LoanInfo.monthsTerm(self)
            return term
        elif self.loanPeriod == 3 : #Weekly
            term = LoanInfo.weeksTerm(self)
            return term
        else :
            term = LoanInfo.daysTerm(self)
            return term #Daily
    
    def monthlyPayment(self):
        nper = LoanInfo.convertPeriod(self)
        rate = LoanInfo.convertInterestRate(self, nper)
        return -1*npf.pmt(rate/100, nper, self.Ammount)

    def loanChart(self):
        chartInfo = dict()
        chartInfo['categories'] = LoanInfo.chartCategories(self)
        chartInfo['interest'] = LoanInfo.chartInterest(self)
        chartInfo['principal'] = LoanInfo.chartPrincipal(self)
        chartInfo['balance'] = LoanInfo.chartBalance(self)
        return chartInfo

    def chartCategories(self) :
        # months = LoanInfo.monthsTerm(self)
        strCategories = ''
        for i in range(LoanInfo.convertPeriod(self)) :
            if self.loanPeriod == 1 :
                newDate = self.StartDate + relativedelta(years=i)
            elif self.loanPeriod == 2 :
                newDate = self.StartDate + relativedelta(months=i)
            elif self.loanPeriod == 3 :
                newDate = self.StartDate + relativedelta(weeks=i)
            else :
                newDate = self.StartDate + relativedelta(days=i)
            strCategories +=  '\'' + str(newDate.date().strftime('%d/%m/%Y')) + '\', '
        return strCategories
    
    def chartInterest(self) :
        # months = LoanInfo.monthsTerm(self)
        mpt = LoanInfo.monthlyPayment(self)
        balance = self.Ammount
        interest = 0
        principal = 0
        strInterest = ''
        interestRate = LoanInfo.convertInterestRate(self, LoanInfo.convertPeriod(self))/100
        for i in range(LoanInfo.convertPeriod(self)) :
            interest = interestRate*balance
            principal = mpt - interest
            balance = balance - principal
            strInterest += str("%.2f" % interest) + ', '
        return strInterest

    def chartPrincipal(self) :
        #months = LoanInfo.monthsTerm(self)
        mpt = LoanInfo.monthlyPayment(self)
        balance = self.Ammount
        interest = 0
        principal = 0
        strPrincipal = ''
        interestRate = LoanInfo.convertInterestRate(self, LoanInfo.convertPeriod(self))/100
        for i in range(LoanInfo.convertPeriod(self)) :
            interest = interestRate*balance
            principal = mpt - interest
            balance = balance - principal
            strPrincipal += str("%.2f" % principal) + ', '
        return strPrincipal

    def chartBalance(self) :
        # months = LoanInfo.monthsTerm(self)
        mpt = LoanInfo.monthlyPayment(self)
        balance = self.Ammount
        interest = 0
        principal = 0
        strBalance = ''
        interestRate = LoanInfo.convertInterestRate(self, LoanInfo.convertPeriod(self))/100
        for i in range(LoanInfo.convertPeriod(self)) :
            interest = interestRate*balance
            principal = mpt - interest
            balance = balance - principal
            strBalance += str("%.2f" % balance) + ', '
        return strBalance