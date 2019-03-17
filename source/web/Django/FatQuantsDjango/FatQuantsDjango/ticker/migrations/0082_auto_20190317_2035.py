# Generated by Django 2.1.7 on 2019-03-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0081_tickereoddata_open_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickereoddata',
            name='high_level',
            field=models.FloatField(blank=True, db_column='high_level', null=True, verbose_name='High'),
        ),
        migrations.AddField(
            model_name='tickereoddata',
            name='low_level',
            field=models.FloatField(blank=True, db_column='low_level', null=True, verbose_name='Low'),
        ),
    ]
