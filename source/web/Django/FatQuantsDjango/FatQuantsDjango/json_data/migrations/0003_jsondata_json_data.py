# Generated by Django 2.1.3 on 2019-02-10 16:09

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_data', '0002_auto_20190210_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsondata',
            name='json_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column='json_data', null=True, verbose_name='JSON Data'),
        ),
    ]
