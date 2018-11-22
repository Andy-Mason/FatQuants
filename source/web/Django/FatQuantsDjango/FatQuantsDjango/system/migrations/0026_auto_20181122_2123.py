# Generated by Django 2.1.3 on 2018-11-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0025_systemauditrecord_field_data_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_boolean',
            field=models.NullBooleanField(db_column='field_value_boolean', verbose_name='Boolean'),
        ),
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_integer',
            field=models.BigIntegerField(blank=True, db_column='field_value_integer', null=True, verbose_name='Integer'),
        ),
    ]
