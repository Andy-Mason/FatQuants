# Generated by Django 2.1.3 on 2018-12-24 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0047_ticker_json_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='TickerIdentifier',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_id', models.ForeignKey(db_column='ticker_id', default=0, on_delete=django.db.models.deletion.CASCADE, to='ticker.Ticker', verbose_name='TickerID')),
            ],
            options={
                'db_table': 'ticker_identifier',
            },
        ),
    ]
