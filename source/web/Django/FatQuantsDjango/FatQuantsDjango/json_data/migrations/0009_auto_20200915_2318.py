# Generated by Django 3.1 on 2020-09-15 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('json_data', '0008_auto_20190211_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jsondata',
            name='json_data',
            field=models.JSONField(blank=True, db_column='json_data', null=True, verbose_name='JSON Data'),
        ),
    ]
