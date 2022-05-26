# Generated by Django 3.2.8 on 2022-05-25 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='DataPlicy',
        ),
        migrations.AddField(
            model_name='profile',
            name='DataPolicy',
            field=models.BooleanField(null=True, verbose_name='Data Policy'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='IdentityDocument',
            field=models.IntegerField(null=True, verbose_name='Identity Document'),
        ),
    ]