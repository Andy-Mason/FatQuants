# Generated by Django 2.1.3 on 2019-02-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0027_delete_batchprocesstasklog'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchProcessTaskIntervention',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'batch_process_task_intervention',
            },
        ),
    ]
