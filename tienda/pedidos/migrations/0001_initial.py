# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 19:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0004_auto_20170722_1555'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CantidadProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.PositiveIntegerField(choices=[(1, 'Recibido'), (2, 'Cancelado'), (3, 'Pagado'), (4, 'Entregado')], default=1)),
                ('tipo_pago', models.PositiveIntegerField(choices=[(1, 'Efectivo'), (2, 'Contra entrega'), (3, 'Tarjeta'), (4, 'Paypal')])),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cantidadproducto',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.Pedido'),
        ),
        migrations.AddField(
            model_name='cantidadproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.Producto'),
        ),
    ]