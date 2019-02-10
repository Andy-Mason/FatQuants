# Generated by Django 2.1.3 on 2019-02-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0023_batchprocesstask_run_finish_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesstask',
            name='run_done_items',
            field=models.PositiveIntegerField(blank=True, db_column='run_done_items', null=True, verbose_name='Done'),
        ),
        migrations.AddField(
            model_name='batchprocesstask',
            name='run_total_items',
            field=models.PositiveIntegerField(blank=True, db_column='run_total_items', null=True, verbose_name='Total'),
        ),
    ]