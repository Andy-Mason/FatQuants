# Generated by Django 2.1.3 on 2019-02-12 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0035_auto_20190212_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesstaskintervention',
            name='intervention_type',
            field=models.SmallIntegerField(choices=[(-1, 'Cancelled'), (0, '<None>'), (1, 'Resumed')], db_column='intervention_type', default=0, verbose_name='InterventionType'),
        ),
    ]
