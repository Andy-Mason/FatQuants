# Generated by Django 2.1.3 on 2018-12-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0041_ticker_listing_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='listing_category',
            field=models.CharField(blank=True, db_column='listing_category', default='', max_length=60, verbose_name='Listing Category'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='listing_date',
            field=models.DateField(blank=True, db_column='listing_date', null=True, verbose_name='Listing Date'),
        ),
    ]
