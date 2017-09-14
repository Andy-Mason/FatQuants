# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-14 19:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_data', '0009_auto_20170914_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsondataitem',
            name='json_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column='json_data', null=True, verbose_name='JSON Data'),
        ),
    ]
