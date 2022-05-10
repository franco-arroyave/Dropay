from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TypeID(models.Model):
    TypeIDID = models.AutoField(primary_key=True)

class xUser(AbstractUser):
    IdentityDocument = models.IntegerField(null=True, verbose_name='Documento de Identidad')
    TypeID = models.ForeignKey('TypeID',on_delete=models.CASCADE)
    DateofBirth = models.DateTimeField(null=True, verbose_name='Cumpleaños')