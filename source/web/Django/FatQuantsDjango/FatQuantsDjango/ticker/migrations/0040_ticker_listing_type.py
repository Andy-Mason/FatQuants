# Generated by Django 2.1.3 on 2018-12-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0039_ticker_trading_exchange_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='listing_type',
            field=models.CharField(blank=True, db_column='listing_type', default='', max_length=20, verbose_name='Listing Type'),
        ),
    ]
