# Generated by Django 2.1.3 on 2018-11-22 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0029_auto_20181122_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_datetime',
            field=models.DateTimeField(blank=True, db_column='field_value_datetime', null=True, verbose_name='DateTime'),
        ),
        migrations.AddField(
            model_name='systemauditrecord',
            name='field_value_duration',
            field=models.DurationField(blank=True, db_column='field_value_duration', null=True, verbose_name='Duration'),
        ),
    ]
