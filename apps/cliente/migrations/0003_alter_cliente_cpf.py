# Generated by Django 3.2.5 on 2021-08-12 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_loja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
