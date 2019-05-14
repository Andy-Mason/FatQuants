# Generated by Django 2.1.7 on 2019-05-14 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0094_ticker_instrument_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='issuer_name',
            field=models.CharField(blank=True, db_column='issuer_name', default='', max_length=100, verbose_name='Issuer Name'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='issuer_type',
            field=models.CharField(blank=True, db_column='issuer_type', default='', max_length=30, verbose_name='Issuer Type'),
        ),
    ]
