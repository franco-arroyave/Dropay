from .loanInfo import LoanInfo
import datetime

class PaymentsInfo :
    def __init__(self, system):
        self.system = system

    
    def paymentSummary(self, lnInfo):
        context = PaymentsInfo.paymentContext(self)
        loanContext = PaymentsInfo.loanContext(self, lnInfo)
        paymentMade = PaymentsInfo.paymentMade(self, context, loanContext)
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
        loanContext = LoanInfo(lnInfo).loanSchedule()
        return loanContext

    def paymentMade(self, paymentCnt, loanCnt):
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