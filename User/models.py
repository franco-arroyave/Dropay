from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TypeID(models.Model):
    TypeIDID = models.AutoField(primary_key=True)
    Description = models.CharField(null=True, max_length=30,verbose_name='Document type')

    def __str__(self):
        return '{}'.format(self.Description)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    IdentityDocument = models.CharField(null=True, max_length=20, verbose_name='Identity Document')
    TypeID = models.ForeignKey(TypeID,on_delete=models.CASCADE, null=True)
    DataPolicy = models.BooleanField(verbose_name='Data Policy', null=True)



    