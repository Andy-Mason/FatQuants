# Generated by Django 2.1.3 on 2018-12-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0035_ticker_issue_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='quote_units',
            field=models.FloatField(blank=True, db_column='quote_units', null=True, verbose_name='Quote Units'),
        ),
    ]
