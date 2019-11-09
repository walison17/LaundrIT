# Generated by Django 2.2.1 on 2019-11-09 00:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_cliente', models.CharField(max_length=50, verbose_name='Nome Cliente')),
                ('rg', models.CharField(blank=True, max_length=14, verbose_name='RG')),
                ('cpf', models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(11111111111)], verbose_name=' CPF- ')),
                ('endereco', models.CharField(max_length=60, verbose_name='Endereço')),
                ('telefone', models.BigIntegerField(blank=True, null=True, verbose_name='Telefone')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]