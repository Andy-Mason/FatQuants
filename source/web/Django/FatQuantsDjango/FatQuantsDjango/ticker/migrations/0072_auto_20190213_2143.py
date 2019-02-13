# Generated by Django 2.1.3 on 2019-02-13 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0071_tickerupdateprocess_last_checked'),
    ]

    operations = [
        migrations.CreateModel(
            name='TickerBatchProcessType',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'ticker_batch_process_type',
            },
        ),
        migrations.AlterUniqueTogether(
            name='tickerupdateprocess',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='tickerupdateprocess',
            name='batch_process_type_id',
        ),
        migrations.RemoveField(
            model_name='tickerupdateprocess',
            name='ticker_id',
        ),
        migrations.DeleteModel(
            name='TickerUpdateProcess',
        ),
    ]
