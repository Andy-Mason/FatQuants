# Generated by Django 2.1.3 on 2018-12-24 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0053_tickerresource'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickerresource',
            name='resource_type',
            field=models.SmallIntegerField(choices=[(0, '<None>'), (1, 'Company website'), (2, 'London Stock Exchange web page'), (3, 'AJ Bell web page')], db_column='resource_type', default=0, verbose_name='Resource Type'),
        ),
        migrations.AlterUniqueTogether(
            name='tickerresource',
            unique_together={('ticker_id', 'resource_type')},
        ),
    ]
