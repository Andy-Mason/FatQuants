# Generated by Django 2.1.3 on 2018-12-24 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0037_productprovider'),
        ('ticker', '0038_ticker_trading_currency_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='trading_exchange_id',
            field=models.ForeignKey(blank=True, db_column='trading_exchange_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_data.TradingExchange', verbose_name='Trading Exchange'),
        ),
    ]
