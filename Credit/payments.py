from .loanInfo import LoanInfo
import datetime

class PaymentsInfo :
    def __init__(self, system):
        self.system = system

    def paymentSummary(self):
        summary = dict()
        principalPaid = 0
        interestPaid = 0
        for payment in self.system:
            principalPaid += payment.Principal
            interestPaid += payment.Interest
            
        summary = {"principalPaid": round(principalPaid, 2),
                   "interestPaid": round(interestPaid, 2),
                   "totalPaid": round(principalPaid, 2) + round(interestPaid, 2)}

        if principalPaid == 0:
            summary["percentagePrincipal"] = 0
            summary["percentageInterest"] = 0
        else:
            summary["percentagePrincipal"] = "%.2f" % (principalPaid / (principalPaid + interestPaid) * 100)
            summary["percentageInterest"] = "%.2f" % (interestPaid / (principalPaid + interestPaid) * 100)
        
        
        return summary

    def paymentsMade(self, lnInfo):
        context = PaymentsInfo.paymentContext(self)
        loanContext = LoanInfo(PaymentsInfo(self).loanContext(lnInfo)).loanSchedule()
        paymentMade = PaymentsInfo.paymentCheck(self, context, loanContext)
        return paymentMade

    def paymentContext(self):
        paymentContext = list()
        for payment in self.system:
            paymentContext.append(payment.__dict__)
        return paymentContext

    def loanContext(self, lnInfo):
        lnInfo["loanPeriod"] = lnInfo["Periodicity_id"]
        lnInfo["StartDate"] = str(lnInfo["StartDate"])
        lnInfo["DisbursementDate"] = str(lnInfo["DisbursementDate"])
        return lnInfo

    def paymentCheck(self, paymentCnt, loanCnt):
        paymentMade = list()
        for loan in loanCnt:
            for payment in paymentCnt:
                if loan["date"] == payment["Date"].strftime("%d/%m/%Y"):
                    loan["check"] = "checked"
                    break
                else :
                    loan["check"] = ""
            paymentMade.append(loan)
        return paymentMade

    def updatePayments(self, lnInfo):
        return 0