# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_auto_20170913_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_name',
            field=models.CharField(db_column='field_name', default='', max_length=63, verbose_name='Field Name'),
        ),
    ]
