# Generated by Django 2.1.3 on 2019-02-10 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0002_auto_20190210_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocesstype',
            name='execution_handler',
            field=models.CharField(db_column='execution_handler', default='', max_length=100, verbose_name='ExecutionHandler'),
        ),
    ]
