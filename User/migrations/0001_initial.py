# Generated by Django 3.2.8 on 2022-05-24 01:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeID',
            fields=[
                ('TypeIDID', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.CharField(max_length=20, null=True, verbose_name='Document type')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IdentityDocument', models.IntegerField(null=True, verbose_name='Documento de Identidad')),
                ('DataPlicy', models.BinaryField(null=True, verbose_name='DataPolicy')),
                ('TypeID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.typeid')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
