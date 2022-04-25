# Generated by Django 3.2.8 on 2022-04-22 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('IdentityDocument', models.IntegerField(verbose_name='Documento de Identidad')),
                ('TypeID', models.CharField(max_length=40, verbose_name='Tipo Documento')),
            ],
        ),
    ]