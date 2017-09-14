# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0004_ticker_identifier_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='description',
            field=models.CharField(db_column='description', default='', max_length=250, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='instrument_type',
            field=models.CharField(blank=True, db_column='instrument_type', max_length=30, null=True, verbose_name='Instrument Type'),
        ),
    ]
