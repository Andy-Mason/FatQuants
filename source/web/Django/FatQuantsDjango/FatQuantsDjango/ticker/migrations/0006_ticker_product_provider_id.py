# Generated by Django 2.1.3 on 2018-12-23 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0037_productprovider'),
        ('ticker', '0005_ticker_instrument_subtype'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='product_provider_id',
            field=models.ForeignKey(blank=True, db_column='product_provider_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='reference_data.ProductProvider', verbose_name='Product Provider'),
        ),
    ]