# Generated by Django 2.1.3 on 2018-12-23 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0010_auto_20181223_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='instrument_type',
            field=models.CharField(blank=True, db_column='instrument_type', default='', max_length=30, verbose_name='Instrument Type'),
        ),
    ]
