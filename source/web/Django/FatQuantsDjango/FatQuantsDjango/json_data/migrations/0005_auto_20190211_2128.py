# Generated by Django 2.1.3 on 2019-02-11 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('json_data', '0004_auto_20190210_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jsondata',
            name='created_timestamp',
        ),
        migrations.RemoveField(
            model_name='jsondata',
            name='json_data',
        ),
        migrations.RemoveField(
            model_name='jsondata',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='jsondata',
            name='updated_timestamp',
        ),
    ]
