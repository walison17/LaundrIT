# Generated by Django 2.2.7 on 2019-11-16 02:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
        ('Pedido', '0019_auto_20191110_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suporte',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=60, verbose_name='E-mail do Cliente')),
                ('cpf', models.BigIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(11111111111)], verbose_name=' CPF- ')),
                ('telefone', models.BigIntegerField(blank=True, null=True, verbose_name='Telefone')),
                ('nome_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.Cliente', verbose_name='Nome do Cliente')),
                ('numero_pedido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Pedido.Pedido', verbose_name='Número do Pedido')),
            ],
        ),
    ]
