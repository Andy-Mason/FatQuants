# Generated by Django 2.1.3 on 2018-12-23 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0036_auto_20181223_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductProvider',
            fields=[
                ('product_provider_id', models.BigAutoField(db_column='product_provider_id', primary_key=True, serialize=False, verbose_name='ProductProviderID')),
                ('description', models.CharField(db_column='description', default='', max_length=100, unique=True, verbose_name='Description')),
            ],
            options={
                'db_table': 'refdata_product_provider',
            },
        ),
    ]
