# Generated by Django 2.0.5 on 2018-05-26 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0014_batchprocesslog'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesslog',
            name='process_operation',
            field=models.SmallIntegerField(blank=True, choices=[(-1, 'Cancel'), (0, '<None>'), (1, 'Run'), (2, 'Resume'), (3, 'ReRun Errors'), (4, 'ReRun All')], db_column='process_operation', null=True, verbose_name='ProcessOperation'),
        ),
    ]
