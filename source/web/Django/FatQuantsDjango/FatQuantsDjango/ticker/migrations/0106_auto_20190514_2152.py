# Generated by Django 2.1.7 on 2019-05-14 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0043_delete_productprovider'),
        ('ticker', '0105_ticker_trading_segment'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='market_sector_id',
            field=models.ForeignKey(blank=True, db_column='market_sector_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='market_sector', to='reference_data.MarketSector', verbose_name='Market Sector'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='morningstar_category_id',
            field=models.ForeignKey(blank=True, db_column='morningstar_category_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='morningstar_category', to='reference_data.MarketSector', verbose_name='Morningstar Category'),
        ),
    ]