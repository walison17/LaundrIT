# Generated by Django 2.2.7 on 2019-11-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0044_auto_20191122_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='preco_unitario',
        ),
        migrations.AddField(
            model_name='item',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=1, editable=False, max_digits=5, verbose_name='valor'),
            preserve_default=False,
        ),
    ]