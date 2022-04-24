from django.db import models

# Create your models here.

class TypeID(models.Model):
    TypeIDID = models.AutoField(primary_key=True)
    Description = models.TextField(null=True, max_length=50)

class Periodicity(models.Model):
    PeriodicityID = models.AutoField(primary_key=True)
    Description = models.TextField(null=True, max_length=50)

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    IdentityDocument = models.IntegerField(null=True, verbose_name='Documento de Identidad')
    TypeID = models.ForeignKey('TypeID',on_delete=models.CASCADE)
    FirstName = models.CharField(null=True, max_length=25, verbose_name='Nombre')
    LastName = models.CharField(null=True, max_length=25, verbose_name='Apellido')
    Email = models.EmailField(null=True, max_length=60, verbose_name='Correo')
    DateofBirth = models.DateTimeField(null=True, verbose_name='Cumpleaños')

class UserCredential(models.Model):
    UserCredentialID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey('User',on_delete=models.CASCADE)
    Username = models.CharField(null=True, max_length=50, verbose_name='Usuario')
    Password = models.CharField(null=True, max_length=50, verbose_name='Contraseña')

class Loan(models.Model):
    LoanID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey('User',on_delete=models.CASCADE)
    Amount = models.FloatField(null=True, verbose_name='Monto')
    Term = models.IntegerField(null=True, verbose_name='Plazo')
    Periodicity = models.ForeignKey('Periodicity',on_delete=models.CASCADE)
    InterestRate = models.FloatField(null=True, verbose_name='Interes')
    StartDate = models.DateTimeField(null=True, verbose_name='Fecha Inicial')
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