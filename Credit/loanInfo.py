import datetime
from this import s
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
        self.DisbursementDate = datetime.datetime.strptime(system.get('DisbursementDate'), '%Y-%m-%d')
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
            months = self.Term / 30.4167
        else :
            months = self.Term
        return months
    
    def weeksTerm(self) :
        self.gralPeriod = 52
        weeks = 0
        if self.termCalendar == "Years":
            weeks = self.Term * 52.1429
        elif self.termCalendar == "Days":
            weeks = self.Term / 7
        else :
            weeks = self.Term * 4.34524
        return int(weeks)
    
    def daysTerm(self) :
        self.gralPeriod = 365
        days = 0
        if self.termCalendar == "Years":
            days = self.Term * 365
        elif self.termCalendar == "Days":
            days = self.Term
        else :
            days = self.Term * 30.4167
        return int(days)

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
        payment = LoanInfo.disbursementInterest(self) + -1*npf.pmt(rate/100, nper, self.Ammount, 0, 0)
        return payment

    def disbursementInterest(self) :
        self.gralPeriod = 365
        interestAmmount = 0
        if self.StartDate != self.DisbursementDate :
            daysInterest = (self.StartDate - self.DisbursementDate).days + 1
            interest = LoanInfo.convertInterestRate(self, daysInterest) / 100
            interestAmmount = (self.Ammount * interest * daysInterest) / LoanInfo.convertPeriod(self)
        return interestAmmount

    def loanChart(self):
        chartInfo = dict()
        chartInfo['categories'] = LoanInfo.chartCategories(self)

        mpt = LoanInfo.monthlyPayment(self)
        balance = self.Ammount
        interest = 0
        interest2 = 0
        principal = 0
        principal2 = 0
        strInterest = ''
        strPrincipal = ''
        strBalance = ''
        interestRate = LoanInfo.convertInterestRate(self, LoanInfo.convertPeriod(self))/100
        for i in range(LoanInfo.convertPeriod(self)) :
            interest = interestRate*balance + LoanInfo.disbursementInterest(self)
            interest2 += interest
            principal = mpt - interest
            principal2 += principal
            balance = balance - principal
            strInterest += str("%.2f" % interest2) + ', '
            strPrincipal += str("%.2f" % principal2) + ', '
            strBalance += str("%.2f" % balance) + ', '
        chartInfo['interest'] = strInterest
        chartInfo['principal'] = strPrincipal
        chartInfo['balance'] = strBalance
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
    

    def loanSchedule(self) :
        scheduleInfo = list()
        interestRate = LoanInfo.convertInterestRate(self, LoanInfo.convertPeriod(self))/100
        balance = self.Ammount
        mpt = LoanInfo.monthlyPayment(self)
        #Date	Payment	Interest	Principal	Balance
        for i in range(LoanInfo.convertPeriod(self)) :
            if self.loanPeriod == 1 :
                newDate = self.StartDate + relativedelta(years=i)
            elif self.loanPeriod == 2 :
                newDate = self.StartDate + relativedelta(months=i)
            elif self.loanPeriod == 3 :
                newDate = self.StartDate + relativedelta(weeks=i)
            else :
                newDate = self.StartDate + relativedelta(days=i)
            interest = interestRate*balance + LoanInfo.disbursementInterest(self)
            principal = mpt - interest
            balance = balance - principal
            scheduleInfo.append({"item" : i + 1,
                                "date" : str(str(newDate.date().strftime('%d/%m/%Y'))), 
                                "payment" : str("%.2f" % mpt), 
                                "interest" : str("%.2f" % interest), 
                                "principal": str("%.2f" % principal), 
                                "balance" : str("%.2f" % balance)})
        return scheduleInfo
    
    def addRegularPayments(self, loanPK, nRegularPayments) :
        regularPayments = list()
        loanSchedule = LoanInfo.loanSchedule(self)
        for i in range(nRegularPayments) :
            regularPayments.append({
                "Date" : datetime.datetime.strptime(loanSchedule[i]['date'], '%d/%m/%Y'),
                "Payment" : loanSchedule[i]['payment'],
                "Interest" : loanSchedule[i]['interest'],
                "Principal" : loanSchedule[i]['principal'],
                "Balance" : loanSchedule[i]['balance'],
                "LoanID" : loanPK
            })
        return regularPayments