# Generated by Django 2.1.7 on 2019-03-17 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0085_auto_20190317_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickereoddata',
            name='open_value',
            field=models.FloatField(blank=True, db_column='open_value', null=True, verbose_name='Open'),
        ),
    ]
