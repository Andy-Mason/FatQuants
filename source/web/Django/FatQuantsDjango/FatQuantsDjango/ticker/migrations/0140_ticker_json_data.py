# Generated by Django 2.1.7 on 2019-05-16 20:15

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0139_auto_20190516_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='json_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column='json_data', null=True, verbose_name='JSON Data'),
        ),
    ]
