# Generated by Django 2.1.3 on 2019-02-12 21:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0036_batchprocesstaskintervention_intervention_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesstaskintervention',
            name='intervention_timestamp',
            field=models.DateTimeField(db_column='intervention_timestamp', default=django.utils.timezone.now, verbose_name='TimeStamp'),
        ),
    ]
