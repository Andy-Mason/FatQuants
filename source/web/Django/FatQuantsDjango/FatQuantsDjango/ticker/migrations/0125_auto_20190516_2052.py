# Generated by Django 2.1.7 on 2019-05-16 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0124_auto_20190516_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticker',
            name='product_leverage',
        ),
        migrations.RemoveField(
            model_name='ticker',
            name='unit_type',
        ),
    ]
