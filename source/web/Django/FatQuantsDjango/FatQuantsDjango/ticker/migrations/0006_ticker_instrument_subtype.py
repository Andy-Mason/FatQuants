# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0005_auto_20170914_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='instrument_subtype',
            field=models.CharField(blank=True, db_column='instrument_subtype', max_length=30, null=True, verbose_name='Instrument Subtype'),
        ),
    ]
