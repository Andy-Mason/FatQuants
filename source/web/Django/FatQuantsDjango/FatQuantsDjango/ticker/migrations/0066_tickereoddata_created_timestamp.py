# Generated by Django 2.1.3 on 2019-02-09 22:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0065_auto_20190209_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickereoddata',
            name='created_timestamp',
            field=models.DateTimeField(db_column='created_timestamp', default=django.utils.timezone.now, verbose_name='Created'),
        ),
    ]