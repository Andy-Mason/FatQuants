# Generated by Django 2.1.3 on 2019-02-10 18:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('batch_process', '0011_auto_20190210_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='batchprocessjsondata',
            name='created_timestamp',
            field=models.DateTimeField(db_column='created_timestamp', default=django.utils.timezone.now, verbose_name='Created'),
        ),
    ]