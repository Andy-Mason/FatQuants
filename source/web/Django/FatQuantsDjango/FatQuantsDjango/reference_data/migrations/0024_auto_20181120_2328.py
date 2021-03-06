# Generated by Django 2.1.3 on 2018-11-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0023_testdata_test_blob'),
    ]

    operations = [
        migrations.CreateModel(
            name='TradingExchange',
            fields=[
                ('trading_exchange_id', models.BigAutoField(db_column='trading_exchange_id', primary_key=True, serialize=False, verbose_name='TradingExchangeID')),
                ('trading_exchange', models.CharField(db_column='trading_exchange', max_length=30, unique=True, verbose_name='TradingExchange')),
            ],
            options={
                'db_table': 'refdata_trading_exchange',
            },
        ),
        migrations.AlterField(
            model_name='marketindex',
            name='market_index',
            field=models.CharField(db_column='market_index', default='', max_length=100, unique=True, verbose_name='MarketIndex'),
        ),
    ]
