# Generated by Django 2.1.3 on 2018-12-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0006_ticker_product_provider_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='product_leverage',
            field=models.FloatField(blank=True, db_column='product_leverage', null=True, verbose_name='Product Leverage'),
        ),
    ]
