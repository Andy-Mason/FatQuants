# Generated by Django 2.1.3 on 2019-02-10 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0013_batchprocesslog'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesslog',
            name='batch_process_id',
            field=models.ForeignKey(db_column='batch_process_id', default=0, on_delete=django.db.models.deletion.CASCADE, to='batch_process.BatchProcess', verbose_name='BatchProcessID'),
        ),
    ]
