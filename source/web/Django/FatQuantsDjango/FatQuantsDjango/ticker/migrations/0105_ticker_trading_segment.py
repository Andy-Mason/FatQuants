# Generated by Django 2.1.7 on 2019-05-14 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0104_auto_20190514_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='trading_segment',
            field=models.CharField(blank=True, db_column='trading_segment', default='', max_length=20, verbose_name='Trading Segment'),
        ),
    ]