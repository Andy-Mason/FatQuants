# Generated by Django 2.1.3 on 2019-02-10 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0025_auto_20190210_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchProcessTaskLog',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'batch_process_task_log',
            },
        ),
    ]