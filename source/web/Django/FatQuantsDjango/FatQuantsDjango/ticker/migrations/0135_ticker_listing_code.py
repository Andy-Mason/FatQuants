# Generated by Django 2.1.7 on 2019-05-16 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0134_ticker_listing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='listing_code',
            field=models.CharField(blank=True, db_column='listing_code', default='', max_length=20, verbose_name='Listing Code'),
        ),
    ]