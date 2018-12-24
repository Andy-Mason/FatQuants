# Generated by Django 2.1.3 on 2018-12-23 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0019_ticker_listing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='listing_code',
            field=models.CharField(blank=True, db_column='listing_code', default='', max_length=20, verbose_name='Listing Code'),
        ),
    ]