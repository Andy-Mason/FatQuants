# Generated by Django 2.1.3 on 2019-02-12 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0037_batchprocesstaskintervention_intervention_timestamp'),
        ('ticker', '0069_tickerupdateprocess'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickerupdateprocess',
            name='batch_process_type_id',
            field=models.ForeignKey(db_column='batch_process_type_id', default=0, on_delete=django.db.models.deletion.PROTECT, to='batch_process.BatchProcessType', verbose_name='BatchProcessTypeID'),
        ),
        migrations.AlterUniqueTogether(
            name='tickerupdateprocess',
            unique_together={('ticker_id', 'batch_process_type_id')},
        ),
    ]
