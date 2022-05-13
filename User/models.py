from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class TypeID(models.Model):
    TypeIDID = models.AutoField(primary_key=True)
    Description = models.CharField(null=True, max_length=20,verbose_name='Document type')

    def __str__(self):
        return '{}'.format(self.Description)

class xUser(AbstractUser):
    IdentityDocument = models.IntegerField(null=True, verbose_name='Documento de Identidad')
    TypeID = models.ForeignKey('TypeID',on_delete=models.CASCADE, null=True)
    DateofBirth = models.DateTimeField(null=True, verbose_name='Cumpleaños')

# class profile(models.Model):
#     User = models.OneToOneField(User, on_delete=models.CASCADE)
#     IdentityDocument = models.IntegerField(null=True, verbose_name='Documento de Identidad')
#     TypeID = models.ForeignKey('TypeID',on_delete=models.CASCADE, null=True)
#     DateofBirth = models.DateTimeField(null=True, verbose_name='Cumpleaños')

    