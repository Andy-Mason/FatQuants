# Generated by Django 2.1.7 on 2019-05-15 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0047_auto_20190515_2121'),
        ('ticker', '0113_auto_20190515_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='quote_currency_id',
            field=models.ForeignKey(blank=True, db_column='quote_currency_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='quote_currency', to='reference_data.Currency', verbose_name='Quote Currency'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='trading_currency_id',
            field=models.ForeignKey(blank=True, db_column='trading_currency_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='trading_currency', to='reference_data.Currency', verbose_name='Trading Currency'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='trading_exchange_id',
            field=models.ForeignKey(blank=True, db_column='trading_exchange_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_data.TradingExchange', verbose_name='Trading Exchange'),
        ),
    ]
