# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0028_auto_20170914_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickereoddata',
            name='high_value',
            field=models.FloatField(blank=True, db_column='high_value', null=True, verbose_name='High'),
        ),
        migrations.AddField(
            model_name='tickereoddata',
            name='low_value',
            field=models.FloatField(blank=True, db_column='low_value', null=True, verbose_name='Low'),
        ),
    ]
