# Generated by Django 2.1.7 on 2019-05-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0123_auto_20190516_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='issuer_name',
            field=models.CharField(blank=True, db_column='issuer_name', default='', max_length=100, verbose_name='Issuer Name'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='issuer_type',
            field=models.CharField(blank=True, db_column='issuer_type', default='', max_length=30, verbose_name='Issuer Type'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='product_leverage',
            field=models.FloatField(blank=True, db_column='product_leverage', null=True, verbose_name='Product Leverage'),
        ),
        migrations.AddField(
            model_name='ticker',
            name='unit_type',
            field=models.CharField(blank=True, choices=[('Acc', 'Accumulation'), ('Inc', 'Income')], db_column='unit_type', default='', max_length=3, verbose_name='Unit Type'),
        ),
    ]
