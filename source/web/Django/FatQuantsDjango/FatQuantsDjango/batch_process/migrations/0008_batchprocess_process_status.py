# Generated by Django 2.1.3 on 2019-02-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0007_auto_20190210_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocess',
            name='process_status',
            field=models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Running...'), (2, 'Finished'), (-1, 'Aborted'), (-2, 'Cancelling...'), (-3, 'Cancelled')], db_column='process_status', default=0, verbose_name='ProcessStatus'),
        ),
    ]
