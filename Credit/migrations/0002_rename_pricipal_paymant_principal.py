# Generated by Django 4.0.4 on 2022-06-08 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Credit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymant',
            old_name='Pricipal',
            new_name='Principal',
        ),
    ]
