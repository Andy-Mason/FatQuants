# Generated by Django 2.1.7 on 2019-07-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0052_currency_base_currency_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='description',
            field=models.CharField(db_column='description', default='', max_length=100, verbose_name='Description'),
        ),
    ]
