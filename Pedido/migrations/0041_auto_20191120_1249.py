# Generated by Django 2.2.7 on 2019-11-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pedido', '0040_auto_20191117_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suporte',
            name='resposta',
            field=models.TextField(default='LaundrIT', max_length=255),
        ),
    ]