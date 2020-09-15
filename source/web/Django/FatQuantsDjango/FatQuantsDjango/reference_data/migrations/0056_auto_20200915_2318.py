# Generated by Django 3.1 on 2020-09-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0055_auto_20190728_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdata',
            name='test_boolean',
            field=models.BooleanField(blank=True, db_column='test_boolean', null=True, verbose_name='Boolean'),
        ),
        migrations.AlterField(
            model_name='testdata',
            name='test_json',
            field=models.JSONField(blank=True, db_column='test_json', null=True, verbose_name='JSON'),
        ),
    ]
