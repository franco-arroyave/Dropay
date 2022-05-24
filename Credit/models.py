from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Periodicity(models.Model):
    PeriodicityID = models.AutoField(primary_key=True)
    Description = models.TextField(null=True, max_length=50)

    def __str__(self):
        return '{}'.format(self.Description)

class Loan(models.Model):
    LoanID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.TextField(null=True, max_length=50, verbose_name="Nombre")
    Ammount = models.FloatField(null=True, verbose_name='Monto')
    Term = models.IntegerField(null=True, verbose_name='Plazo')
    Periodicity = models.ForeignKey(Periodicity,on_delete=models.CASCADE)
    InterestRate = models.FloatField(null=True, verbose_name='Interes')
    StartDate = models.DateField(null=True, verbose_name='Fecha Inicial')
    DisbursementDate = models.DateField(null=True, verbose_name='Fecha Desembolso')
    monthlyPayment = models.FloatField(null=True, verbose_name='Cuota')

class xPayment(models.Model):
    xPaymentID = models.AutoField(primary_key=True)
    LoanID = models.ForeignKey(Loan, on_delete=models.CASCADE)
    Date = models.DateTimeField(null=True, verbose_name='Fecha de Pago')
    Amount = models.FloatField(null=True, verbose_name='Monto')

class Paymant(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    LoanID = models.ForeignKey(Loan, on_delete=models.CASCADE)
    Date = models.DateTimeField(null=True, verbose_name='Fecha de Pago')
    Payment = models.FloatField(null=True, verbose_name='Valor Pago')
    Pricipal = models.FloatField(null=True, verbose_name='Capital')
    Interest = models.FloatField(null=True, verbose_name='Interes')
    Balance = models.FloatField(null=True, verbose_name='Balance')