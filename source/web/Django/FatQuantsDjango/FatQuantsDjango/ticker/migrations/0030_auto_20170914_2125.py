# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0029_auto_20170914_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickereoddata',
            name='close_value',
            field=models.FloatField(blank=True, db_column='close_value', null=True, verbose_name='Close'),
        ),
        migrations.AddField(
            model_name='tickereoddata',
            name='volume',
            field=models.FloatField(blank=True, db_column='volume', null=True, verbose_name='Volume'),
        ),
    ]
