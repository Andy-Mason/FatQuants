# Generated by Django 2.1.7 on 2019-03-17 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticker', '0084_auto_20190317_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickereoddata',
            name='close_level',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='created_timestamp',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='high_level',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='low_level',
        ),
        migrations.RemoveField(
            model_name='tickereoddata',
            name='open_level',
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
