# Generated by Django 2.1.3 on 2019-02-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0021_auto_20190210_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesstask',
            name='run_start_time',
            field=models.DateTimeField(blank=True, db_column='run_start_time', null=True, verbose_name='StartTime'),
        ),
    ]
