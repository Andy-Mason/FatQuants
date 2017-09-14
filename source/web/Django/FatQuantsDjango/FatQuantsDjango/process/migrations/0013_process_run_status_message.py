# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0012_process_run_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='run_status_message',
            field=models.CharField(blank=True, db_column='run_status_message', default='', max_length=100, null=True, verbose_name='StatusMessage'),
        ),
    ]
