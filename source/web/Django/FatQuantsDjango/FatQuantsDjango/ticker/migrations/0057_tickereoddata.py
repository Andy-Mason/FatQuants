# Generated by Django 2.1.3 on 2019-02-09 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0056_auto_20190209_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='TickerEodData',
            fields=[
                ('ticker_eod_data_id', models.BigAutoField(db_column='ticker_eod_data_id', primary_key=True, serialize=False, verbose_name='TickerEodDataID')),
            ],
        ),
    ]
