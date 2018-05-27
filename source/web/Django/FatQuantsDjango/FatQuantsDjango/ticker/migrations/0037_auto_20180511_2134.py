# Generated by Django 2.0.5 on 2018-05-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0036_auto_20180511_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('Acc', 'Accumulation'), ('Inc', 'Income')], db_column='unit_type', default='', max_length=3, verbose_name='Unit Type'),
        ),
    ]
