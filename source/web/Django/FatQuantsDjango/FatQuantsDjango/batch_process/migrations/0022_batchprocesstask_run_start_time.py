# Generated by Django 2.0.5 on 2018-05-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0021_auto_20180526_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesstask',
            name='run_start_time',
            field=models.DateTimeField(blank=True, db_column='run_start_time', null=True, verbose_name='StartTime'),
        ),
    ]