# Generated by Django 2.1.3 on 2019-02-09 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0061_auto_20190209_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickereoddata',
            name='data_source',
            field=models.SmallIntegerField(choices=[(0, '<None>'), (1, 'File')], db_column='data_source', default=0, verbose_name='Data Source'),
        ),
    ]
