from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TypeID(models.Model):
    TypeIDID = models.AutoField(primary_key=True)

class xUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    IdentityDocument = models.IntegerField(null=True, verbose_name='Documento de Identidad')
    TypeID = models.ForeignKey('TypeID',on_delete=models.CASCADE)
    DateofBirth = models.DateTimeField(null=True, verbose_name='Cumpleaños')