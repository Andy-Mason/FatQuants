# Generated by Django 2.1.3 on 2019-02-10 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('json_data', '0003_jsondata_json_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='jsondata',
            name='created_timestamp',
            field=models.DateTimeField(db_column='created_timestamp', default=django.utils.timezone.now, verbose_name='Created'),
        ),
        migrations.AddField(
            model_name='jsondata',
            name='updated_timestamp',
            field=models.DateTimeField(blank=True, db_column='updated_timestamp', default=django.utils.timezone.now, null=True, verbose_name='Updated'),
        ),
    ]