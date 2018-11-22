# Generated by Django 2.1.3 on 2018-11-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0028_systemauditrecord_field_value_decimal'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_date',
            field=models.DateField(blank=True, db_column='field_value_date', null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_time',
            field=models.TimeField(blank=True, db_column='field_value_time', null=True, verbose_name='Time'),
        ),
    ]
