# Generated by Django 3.2.6 on 2021-08-05 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.FloatField(max_length=10)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='categoria.category')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.store')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Itens',
            },
        ),
    ]
