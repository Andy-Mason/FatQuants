# Generated by Django 2.1.7 on 2019-03-17 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0079_tickerbatchprocess_last_checked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickereoddata',
            name='close_value',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='created_timestamp',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='high_value',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='low_value',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='open_value',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='updated_timestamp',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='volume',
        ),
    ]
