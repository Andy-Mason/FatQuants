# Generated by Django 2.1.3 on 2018-12-24 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0031_auto_20181224_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticker',
            name='product_leverage',
            field=models.FloatField(blank=True, db_column='product_leverage', null=True, verbose_name='Product Leverage'),
        ),
    ]
