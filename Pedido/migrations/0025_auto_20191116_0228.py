# Generated by Django 2.2.7 on 2019-11-16 05:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0024_auto_20191116_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suporte',
            name='cpf',
            field=models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(11111111111)], verbose_name=' CPF '),
        ),
    ]