# Generated by Django 2.1.3 on 2018-11-20 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0003_auto_20181120_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='base_currency_id',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='base_currency_units',
        ),
    ]
