# Generated by Django 2.1.7 on 2019-07-28 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0048_auto_20190728_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='crypto_currency',
            field=models.BooleanField(db_column='crypto_currency', default=False, verbose_name='CryptoCurrency'),
        ),
    ]
