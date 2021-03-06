# Generated by Django 2.1.7 on 2019-05-15 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0107_ticker_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticker',
            name='exchange_market_size',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='instrument_type',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='issue_size',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='issuer_name',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='issuer_type',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='json_data',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='listing_category',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='listing_code',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='listing_date',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='listing_type',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='market_sector_id',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='morningstar_category_id',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='product_leverage',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='quote_currency_id',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='quote_units',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='registered_country_id',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='security_name',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='security_type',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='trading_currency_id',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='trading_exchange_id',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='trading_segment',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='trading_service',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='unit_type',
        ),
    ]
