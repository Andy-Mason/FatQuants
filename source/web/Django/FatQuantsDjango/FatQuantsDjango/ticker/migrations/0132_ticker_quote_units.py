# Generated by Django 2.1.7 on 2019-05-16 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0131_auto_20190516_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='quote_units',
            field=models.FloatField(blank=True, db_column='quote_units', null=True, verbose_name='Quote Units'),
        ),
    ]
