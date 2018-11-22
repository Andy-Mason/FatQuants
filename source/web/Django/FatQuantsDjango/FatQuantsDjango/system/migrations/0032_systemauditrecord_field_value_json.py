# Generated by Django 2.1.3 on 2018-11-22 21:25

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0031_systemauditrecord_field_value_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column='field_value_json', null=True, verbose_name='JSON'),
        ),
    ]