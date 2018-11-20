# Generated by Django 2.1.3 on 2018-11-20 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0016_testdata_test_integer'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdata',
            name='test_bigint',
            field=models.BigIntegerField(blank=True, db_column='test_bigint', null=True, verbose_name='Big Integer'),
        ),
        migrations.AddField(
            model_name='testdata',
            name='test_float',
            field=models.FloatField(blank=True, db_column='test_float', null=True, verbose_name='Float'),
        ),
    ]
