# Generated by Django 2.1.3 on 2018-11-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_data', '0019_auto_20181120_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdata',
            name='test_datetime',
            field=models.DateTimeField(blank=True, db_column='test_datetime', null=True, verbose_name='DateTime'),
        ),
        migrations.AddField(
            model_name='testdata',
            name='test_duration',
            field=models.DurationField(blank=True, db_column='test_duration', null=True, verbose_name='Duration'),
        ),
        migrations.AddField(
            model_name='testdata',
            name='test_text',
            field=models.TextField(blank=True, db_column='test_text', null=True, verbose_name='Text'),
        ),
    ]
