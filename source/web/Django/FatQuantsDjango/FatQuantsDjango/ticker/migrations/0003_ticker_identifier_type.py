# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0019_tradingexchange'),
        ('ticker', '0002_ticker_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='identifier_type',
            field=models.ForeignKey(db_column='identifier_type', default='', on_delete=django.db.models.deletion.PROTECT, to='reference_data.IdentifierType', verbose_name='IdentifierType'),
        ),
    ]
