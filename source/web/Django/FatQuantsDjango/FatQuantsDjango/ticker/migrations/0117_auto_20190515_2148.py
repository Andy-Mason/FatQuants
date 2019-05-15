# Generated by Django 2.1.7 on 2019-05-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0116_ticker_listing_code'),
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
