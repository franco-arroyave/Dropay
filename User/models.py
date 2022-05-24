from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TypeID(models.Model):
    TypeIDID = models.AutoField(primary_key=True)
    Description = models.CharField(null=True, max_length=20,verbose_name='Document type')

    def __str__(self):
        return '{}'.format(self.Description)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    IdentityDocument = models.IntegerField(null=True, verbose_name='Documento de Identidad')
    TypeID = models.ForeignKey('TypeID',on_delete=models.CASCADE, null=True)
    DataPlicy = models.BinaryField('DataPolicy', null=True)



    